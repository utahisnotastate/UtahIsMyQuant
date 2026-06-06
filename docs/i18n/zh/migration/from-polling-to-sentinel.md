# 迁移：轮询 / REST → Sentinel（WebSocket）

## 你属于这里若…

- 价格通过 `requests.get()`、cron 或 1–5 秒轮询循环到达
- 交易台「实时」指「股票刷新够快」
- MDH 团队拥有 40 个调用同一 REST 端点的 Python 脚本

## 变化

| 之前 | 之后 |
|------|------|
| 定时拉取 | tick 推送（`websockets`） |
| 热路径阻塞 I/O | `asyncio` 队列解耦网络与逻辑 |
| 延迟 = 轮询周期 + RTT | 延迟 = 仅处理（见 `latency_us`） |

## 切换步骤

### 1. 镜像你的数据源格式

将供应商 JSON 映射到 `Tick.from_payload`：

```python
# Vendor: {"ticker": "SPY", "last": 450.12, "size": 100}
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

或在 `tick_observer.py` 中扩展 `from_payload` 以支持你的键。

### 2. 在轮询旁启动 sentinel（第 1–2 周）

```python
observer = TickObserver(uri="wss://vendor/stream")
observer.subscribe(log_only_handler)  # no execution
observer.start_sentinel()
```

保留遗留轮询器；比较时间戳与最新价。

### 3. 测量慢数据税

每 tick 记录 `TickObserver.latency_us(tick)`。若负载下 p99 > 200ms，supervisor 将触发 circuit breaker——**这是有意设计**。

### 4. 退役轮询器（第 3 周+）

- 生产逻辑仅经 `observer.ingest` 或 WebSocket
- 退役 cron；仅保留一个 EOD 对账批处理

## 陷阱

| 陷阱 | 修复 |
|------|------|
| WebSocket 重连风暴 | 在 `listen()` 外包装指数退避（你的适配器） |
| 部分消息 | 在 `queue.put` 前验证 JSON |
| 标的映射漂移 | 集中符号表 |
| 遗留同步应用中的 asyncio | 在独立进程运行循环（OmegaPoint 模式） |

## 回滚计划

30 天内保留只读轮询器。若 sentinel 失败，回退到轮询日志——非静默失败。

## 下一步

- [重度回测 → 实时](from-backtest-heavy-to-realtime.md)
- [技术架构](../technical-architecture.md)
