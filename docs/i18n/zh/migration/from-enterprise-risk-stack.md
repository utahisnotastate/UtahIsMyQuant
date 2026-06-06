# 迁移：企业风险技术栈 → UtahIsMyQuant Supervisor

## 你属于这里若…

- 通过供应商 RMS 做交易前合规（限额、胖手指、限制名单）
- 日内风险在独立 Java 服务
- 紧急停止归运营而非量化代码

## UtahIsMyQuant 不是什么

- 不是**监管**合规（限制证券、洗售等）的替代
- 不是认证 **VaR** 引擎
- 不是 SEC 检查的审计软件

## 它是什么

- 与 tick 流对齐的**低延迟战术保镖**
- 对 bug（亏损）与 fix（止损）统一的 **Fourth Law** 暂停
- 数据 plenum 上的 **Circuit breaker**（延迟代理）

## 分层风险模型（推荐）

```text
┌─────────────────────────────────────┐
│  Enterprise RMS (vendor) — MUST keep │
├─────────────────────────────────────┤
│  UtahIsMyQuant RiskSupervisor        │
├─────────────────────────────────────┤
│  AlphaGenerator LogicGateMatrix      │
├─────────────────────────────────────┤
│  Execution algos / broker            │
└─────────────────────────────────────┘
```

**规则：** 冲突时企业 RMS 优先。亚秒抽动由 supervisor 优先。

## 控制映射

| 企业 RMS | RiskSupervisor |
|----------|----------------|
| 总敞口限额 | `monitor_exposure` + `max_position_size` |
| 止损 / 跟踪 | `enforce_stop_loss` |
| 策略紧急停止 | `circuit_breaker_active` |
| 模型覆盖 | `veto_decision` → WAIT |
| 压力情景 | 未内置——保留供应商工具 |

## 集成模式

```python
def pre_send_order(event: AlphaEvent, enterprise_ok: bool) -> bool:
    if not enterprise_ok:
        return False
    if event.circuit_breaker:
        return False
    if event.supervisor_verdict in ("VETO", "FORCE_STOP"):
        return False
    return event.decision["action"].startswith("EXECUTE_")
```

## 切换检查清单

- [ ] 记录双重批准：运营紧急停止 + `reset_circuit_breaker()` ACL
- [ ] 将 position dict 格式映射到 `RiskSupervisor.update_positions`
- [ ] 对 `// CIRCUIT BREAKER TRIPPED` 日志行告警（SIEM）
- [ ] 月度演练：强制高延迟 → 验证零新订单

## 陷阱

- 因「supervisor 够了」而移除企业 RMS——**不要**
- 在合规归档中忽视 `gates_failed=supervisor`

## 下一步

- [经理指南](../guides/hedge-fund-manager.md)
