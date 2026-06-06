# 教程 08：实时 WebSocket 数据源

## 目标

将真实 `wss://` tick 数据源连接到 Sentinel observer。

## 前置条件

- 数据供应商的 WebSocket URL
- 已安装 `websockets`

## 运行

```bash
py omega_point.py --uri wss://YOUR_FEED_URL --live
```

或：

```bash
py main.py --uri wss://YOUR_FEED_URL --live
```

## 规范化 JSON

若需要，扩展 `Tick.from_payload`：

```python
# src/tick_observer.py — add keys your vendor uses
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

## 安全

1. **仅模拟交易**直至验证否决行为
2. 将所有 `EXECUTE_*` 记录到文件
3. 根据网络设置合适的 `max_latency_ms`

## 下一步

[教程 09：自定义券商适配器](09-custom-broker-adapter.md)
