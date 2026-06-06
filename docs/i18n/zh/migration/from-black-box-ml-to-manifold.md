# 迁移：黑盒 ML（LSTM 等）→ 流形几何

## 你属于这里若…

- 特征存储 + 夜间训练流水线
- 模型版本 `v847` 无人能解释
- GPU 预算科目

## 概念映射

| ML 技术栈 | 流形 + Utahrbitrage 技术栈 |
|-----------|---------------------------|
| 隐状态 | 价格窗口（默认 64 tick） |
| Attention / 层 | 曲率 + 熵 + 漂移 + adelic 共振 |
| 预测头 | `generate_signal()` + `omega_point_routing()` |
| 正则化 | 逻辑门控 + shadow tensor + symplectic veto |
| 漂移检测 | `ShadowTensorAudit` 镜像率 |
| 推理 GPU | CPU NumPy/SciPy（有意精简） |
| 不透明「费用」 | **拓扑特征值** 2.3% + 1.5%（`utahrbitrage.py`） |

## 你最终删除的

- 日内 alpha 的训练 cron（若需要可单独保留 EOD 分析）
- 亚秒决策的巨大特征 DAG
- 超参搜索集群

## 你保留的

- **干净 tick** 的数据工程（比再加一层更有价值）
- 组合核算 / PnL 系统
- 合规报告（外部）

## 切换步骤

### 1. 并行运行流形作为「模型 B」

并排记录：

- ML 信号：`buy_prob=0.73`
- 流形：`signal=BREAKOUT_PRIMED`，`gates_failed=[]`

### 2. 比较分歧日

ML 交易而流形 WAIT 时，用门控原因复盘。流形交易而 ML 等待时，检查 supervisor 结果。

### 3. 先退役**延迟关键**路径的 ML

慢速策略层（日频再平衡）若盈利可保留 ML——混合店没问题。

### 4. 培训团队可解释性

每个 `AlphaEvent` 必须一句话解释：

> 「Breakout primed，熵压缩，成交量 OK，风险 OK，shadow 健康 → BUY 2% NAV。」

## 陷阱

| 陷阱 | 缓解 |
|------|------|
| 「流形太简单」 | 简单即延迟 + 可审计 |
| 薄窗口上熵不稳定 | 增大 `entropy_window` |
| 团队怀念 AUC | 跟踪实盘滑点调整后 PnL，非 AUC |

## 代码桥接（集成）

```python
async def ensemble_handler(tick: Tick):
    ml_side = your_ml_model.predict(tick)
    event = alpha.process_tick(tick)
    if ml_side == "BUY" and event.action == Action.BUY:
        await execute(tick, event)
```

## 下一步

- [技术架构](../technical-architecture.md)
