# 移行: エンタープライズリスクスタック → UtahIsMyQuant スーパーバイザー

## 該当する場合…

- ベンダー RMS による取引前コンプライアンス（限度、ファットフィンガー、制限リスト）
- 別 Java サービスでの日中リスク
- オペが所有するキルスイッチ、クオントコードではない

## UtahIsMyQuant が **ではない** もの

- **規制** コンプライアンスの置き換え（制限銘柄、ウォッシュセール等）
- 認定 **VaR** エンジン
- SEC 審査用監査ソフト

## **である** もの

- ティックストリームに整合した **低遅延戦術ボディガード**
- バグ（損失）と修正（停止）の両方で停止する **Fourth Law** 統合停止
- データ plenum（遅延プロキシ）での **サーキットブレーカー**

## レイヤードリスクモデル（推奨）

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

**ルール:** 衝突時はエンタープライズ RMS が勝つ。サブ秒の twitch ではスーパーバイザーが勝つ。

## コントロールのマッピング

| エンタープライズ RMS | RiskSupervisor |
|----------------|----------------|
| グロスエクスポージャー上限 | `monitor_exposure` + `max_position_size` |
| ストップロス / トレーリング | `enforce_stop_loss` |
| 戦略キルスイッチ | `circuit_breaker_active` |
| モデル上書き | `veto_decision` → WAIT |
| ストレスシナリオ | 組み込みなし — ベンダーツールを維持 |

## 統合パターン

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

## 切り替えチェックリスト

- [ ] 二重承認を文書化: オペキルスイッチ + `reset_circuit_breaker()` ACL
- [ ] ポジション辞書形式を `RiskSupervisor.update_positions` にマップ
- [ ] `// CIRCUIT BREAKER TRIPPED` ログ行でアラート（SIEM）
- [ ] 月次訓練: 高遅延を強制 → 新規注文ゼロを検証

## 落とし穴

- 「スーパーバイザーで十分」としてエンタープライズ RMS を削除 — **しない**
- コンプライアンスアーカイブで `gates_failed=supervisor` を無視

## 次へ

- [マネージャーガイド](../guides/hedge-fund-manager.md)
