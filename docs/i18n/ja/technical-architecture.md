# 技術アーキテクチャ

## システム概要

UtahIsMyQuant は **閉ループイベント駆動スタック** を実装します:

```text
┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ TickObserver │────▶│  AlphaGenerator │────▶│  RiskSupervisor  │
│  (ingest)    │     │ (logic gates)   │◀────│  (veto / exit)   │
└──────┬───────┘     └────────┬────────┘     └──────────────────┘
       │                      │
       │              ┌───────▼────────┐
       │              │ ManifoldEngine │
       │              │ ShadowTensor   │
       │              └────────────────┘
       │
       ▼
  WebSocket / Replay queue
```

エントリポイント:

- `omega_point.py`（`OmegaPoint`）— クラシック閉ループ
- `main.py`（`OmniDiscoveryEngine`）— Omni/TAD/symplectic + utah-flux

---

## モジュールリファレンス

### `manifold_kernel.py` — ManifoldEngine（+ adelic）

**責務:** 価格ウィンドウからの特徴抽出。

| メソッド | 入力 | 出力 | 備考 |
|--------|-------|--------|-------|
| `calculate_curvature` | `price_vector` | `float` | 2 次差分の平均絶対値 |
| `manifold_drift` | `price_vector` | `float` | 3 次差分の平均（加速） |
| `differential_entropy` | `price_vector` | `float` | 対数リターンの KDE |
| `adaptive_quantize` | `price_vector` | `ndarray` | 平静時 `float64` / 変動時 `float32` |
| `adelic_resonance` | prices, volumes | `float` | クロスプライム共鳴強度 |
| `detect_adelic_void` | prices, volumes | `bool` | 流動性真空検出 |
| `generate_signal` | curvature, entropy, drift, adelic state | `str` | シグナル列挙（`ADELIC_*` 含む） |

**デフォルト感度:** `0.05`（`REVERSAL_IMMINENT` の曲率閾値）。

**シグナル優先度**（最初の一致が勝つ）:

1. `REVERSAL_IMMINENT` — 曲率 > sensitivity
2. `DRIFT_ACCELERATING` / `DRIFT_DECELERATING` — |drift| > `drift_sensitivity`（1e-3）
3. `BREAKOUT_PRIMED` — エントロピー < ベースラインの 85%
4. `HOLD`

---

### `tick_observer.py` — TickObserver

**責務:** 非同期取り込みとファンアウト。

| モード | API | 用途 |
|------|-----|----------|
| Sentinel | `listen()` + `process()` / `start_sentinel()` | ライブ WebSocket |
| Replay | `ingest(payload)` + `process()` | シミュレーション |
| Bridge | `listen_queue(external_queue)` | レガシー統合 |

**Tick スキーマ:**

```python
Tick(symbol: str, price: float, volume: float = 0, timestamp_ns: int)
```

**ペイロードエイリアス:** `symbol`/`s`, `price`/`p`, `volume`/`v`。

**遅延:** `TickObserver.latency_us(tick)` → ティックタイムスタンプからのマイクロ秒。

---

### `shadow_tensor.py` — ShadowTensorAudit

**責務:** 逆マニフォールド鏡写しによるアルファ劣化検出。

- 価格ウィンドウを反射: `reflected = 2 * anchor - prices`
- 順方向シグナルと逆方向シグナルを比較
- `degradation_score` = ローリングウィンドウ上のミラー率
- `alpha_healthy()` はスコア < `mirror_threshold`（デフォルト 0.55）のとき

バックグラウンドスレッド: `start_background(interval=0.5)`。

---

### `alpha_generator.py` — AlphaGenerator

**責務:** ロジックゲート決定行列 + PnL/タイス会計、オプションの Omni フック（TAD、symplectic、utah-flux）。

**LogicGateMatrix ゲート:**

| ゲート | キー | 合格条件 |
|------|-----|----------------|
| Curvature | `curvature` | 取引可能シグナル + 大きさルール |
| Volume | `volume` | `volume >= min_volume` |
| Risk | `risk` | `exposure/capital < risk_limit`（デフォルト 2%） |
| Shadow | `shadow` | `shadow_healthy == True` |

**ゲート後のスーパーバイザー拒否**（`supervisor` 接続時）: `gates_failed` に `supervisor` を追加可能。

**実行動詞:** `WAIT`, `EXECUTE_BUY`, `EXECUTE_SELL`, `EXECUTE_EXIT`。

**タイス:** 正の PnL に `TITHE_RATE = 0.10` → `tithe_allocation()` 経由で `FOOD` / `WATER` バケツ。

---

### `risk_supervisor.py` — RiskSupervisor

**責務:** ポートフォリオレベルのボディガード（Fourth Law 境界）。

| 制御 | デフォルト | 効果 |
|---------|---------|--------|
| `max_drawdown` | 5% | ポジションごと `SELL_IMMEDIATE` |
| `max_position_size` | 10% | 総エクスポージャー上限 |
| `max_latency_ms` | 200 | サーキットブレーカー |
| `max_account_drawdown` | 5% | 口座レベル停止 |

**Fourth Law:** `fourth_law_boundary(bug, fix)` → どちらか true で停止。

**統合:** `evaluate_tick()` → `veto_decision()` がアルファ decision 辞書を変更。

---

## データフロー（単一ティック）

```text
1. WebSocket recv → JSON → queue.put
2. process() → Tick.from_payload → emit()
3. AlphaGenerator.process_tick:
   a. 価格/出来高を追加、ウィンドウをトリム（デフォルト 64）
   b. ManifoldEngine 特徴量
   c. ShadowTensorAudit.record_tick（オプション）
   d. generate_action（ロジックゲート）
   e. RiskSupervisor.evaluate_tick + veto_decision
   f. decision_to_action → PnL + tithe
4. AlphaEvent がサブスクライバー / OmegaPoint ログへ返る
```

---

## 設定マトリックス

| パラメータ | 場所 | 典型的な範囲 |
|-----------|----------|---------------|
| `sensitivity` | ManifoldEngine | 0.01–0.10 |
| `entropy_window` | ManifoldEngine | 16–64 |
| `risk_limit` | AlphaGenerator / LogicGateMatrix | 0.01–0.05 |
| `capital` | AlphaGenerator | 口座 NAV |
| `min_volume` | LogicGateMatrix | 取引所依存 |
| `max_drawdown` | RiskSupervisor | 0.02–0.08 |
| `max_position_size` | RiskSupervisor | 0.05–0.25 |
| `max_latency_ms` | RiskSupervisor | 50–500 |

---

## 依存関係

```text
numpy, scipy    — manifold + adelic math
websockets      — live sentinel
asyncio         — stdlib event loop
streamlit       — Omni-Sieve dashboard (optional)
pytest          — test harness
```

---

## テスト

```bash
pytest -q                           # 62 tests
pytest tests/test_manifold.py -v    # kernel only
pytest tests/test_alpha_gates.py -v # gates only
pytest tests/test_risk_supervisor.py -v
pytest tests/test_omega_point.py -v # integration
```

---

## 拡張ポイント

1. **ブローカーアダプター** — `TickObserver` を購読、`AlphaEvent.action` で注文送信
2. **カスタムフィード** — 自前 JSON スキーマで `ingest()` を実装（`from_payload` を拡張）
3. **追加ゲート** — `LogicGateMatrix.evaluate()` をサブクラス化、または `generate_action` をラップ
4. **ディストレスオーバーレイ** — 外部 Akashic/ディストレス信号をスーパーバイザー入力に追加（`data/`）

---

## セキュリティと運用の注意

- API キーや認証情報入り `.env` をコミットしない
- 拒否/停止動作を検証するまでペーパートレードのみでライブ実行
- サーキットブレーカーは遅延ベースのプロキシであり、取引所ステータスフィードではない
- HA/クラスタリングなし — 単一プロセス asyncio モデル

---

## 関連ドキュメント

- [API リファレンス](api-reference.md)
- [クオント日次ワークフロー](guides/quant-daily-workflow.md)
- [移行ガイド](migration/README.md)
