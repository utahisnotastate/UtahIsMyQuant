# クオント日次ワークフロー — UtahIsMyQuant を実生活に統合する

ラップトップ上のもう一つの放置リポジトリにしない、**毎取引日** の使い方です。

---

## 朝（プレマーケット、30–45分）

### 1. 健全性チェック

```powershell
cd UtahIsMyQuant
.venv\Scripts\activate
pytest -q
```

赤なら: **取引しない**。まずテストを直す — 6ヶ月前に理解をやめた数学を守っている。

### 2. 一晩のログを確認

昨日のログで検索:

| パターン | アクション |
|---------|--------|
| `CIRCUIT BREAKER TRIPPED` | フィード遅延 / VPS ネットワークを確認 |
| `gates_failed': ['shadow']` | アルファがノイズを鏡写し — サイズ縮小または一時停止 |
| `FORCE_STOP` | 銘柄ごとに事後分析 |
| ほぼ `WAIT` | 正常。100% EXECUTE は不審 |

### 3. 今日のパラメータを設定（書き留める）

```python
engine = ManifoldEngine(sensitivity=0.05)  # セッション中は変更しない
gen = AlphaGenerator(
    capital=YOUR_NAV,
    risk_limit=0.02,
    min_volume=YOUR_VENUE_MIN,
    supervisor=RiskSupervisor(max_latency_ms=200),
)
```

**ルール:** ライブでは週にパラメータ変更は最大1つ。さもなくば実資金でバックテストしている。

### 4. Sentinel 起動（最初15分はログのみ）

```python
# omega_point.py または自前ラッパー
omega = OmegaPoint(uri=os.environ["WSS_URI"], capital=NAV)
# 最初15分: execute() をログのみにパッチ
```

`latency_us` p99 < 200ms を確認。

---

## 市場時間（継続）

### イベントループの心のモデル

```text
tick → manifold features → gates → supervisor → your broker adapter
```

### あなたの仕事は上書きではない

週2回以上上書きするなら、システムが誤設定 — パラメータを直し、ヒーロートレードしない。

### クイック診断スニペット

```python
event = gen.process_tick(tick)
if event:
    print(event.signal, event.action, event.gates_failed, event.supervisor_verdict)
```

### 昼チェック（5分）

- 口座ドローダウン vs `max_account_drawdown`
- アクションが WAIT なのにエクスポージャーが残った銘柄（同期バグ？）
- タイス積算（`tithe_allocation()`）— 健全性確認のみ

---

## 午後（引け前）

### 1. フラット方針

デスクルールを決める:

- `DRIFT_DECELERATING` で **自動 EXIT**（すでにバイアスあり）
- T-15分でハードフラット — ブローカーの cron、UtahIsMyQuant ではない

### 2. `AlphaEvent` ログをエクスポート

追記のみ JSONL 推奨:

```python
import json
with open("logs/session.jsonl", "a") as f:
    f.write(json.dumps(event.__dict__, default=str) + "\n")
```

### 3. きれいにシャットダウン

```python
omega.shutdown()  # shadow スレッド + supervisor スレッドを停止
```

---

## 週次（バックテスト劇なしの研究）

| 曜日 | タスク |
|-----|------|
| 月 | ゲート失敗ヒストグラムをレビュー |
| 水 | パラメータ変更を1つペーパーテスト |
| 金 | 最悪取引の3文事後分析を書く |

**許可される研究:**

- 遅延分布プロット
- ミラー率 vs 実現スリッページ
- 出来高ゲート校正

**禁止される研究:**

- 今日のライブ変更を正当化する「2019年でもう1回バックテスト」

---

## ブローカー配線（パターン）

```python
async def guarded_execute(tick: Tick, event: AlphaEvent):
    if event.action not in (Action.BUY, Action.SELL, Action.EXIT):
        return
    if event.circuit_breaker:
        return
    await broker.send(symbol=tick.symbol, side=event.action.value, qty=size_from(event))
```

**べき等** な注文 ID を維持。スーパーバイザーは変動ティックで重複 EXIT を出しうる — 自側で重複排除。

---

## 「普通のクオント生活」との統合

| 活動 | UtahIsMyQuant の役割 |
|----------|-------------------|
| 朝のリサーチ読み | `min_volume` に反映、裁量上書きではない |
| マクロカレンダー | 手動一時停止: 自ら新規エントリーを止めた後のみ `supervisor.reset_circuit_breaker()` |
| Slack アラート | `EXECUTE_*` と `FORCE_STOP` をフック |
| Jupyter 探索 | `ingest` でオフラインリプレイ、ライブループと混ぜない |
| 週末 ML 学習 | 別パイプライン；重みをマニフォールドにマージしない |

---

## 損失したとき

1. その取引の `gates_failed` を引く
2. スーパーバイザー拒否が発火して無視していないか確認
3. 全ゲート緑で負けた: **正常**
4. 同日に `risk_limit` を上げない

---

## 儲かったとき

可能なら作者に: **PayPal utah@utahcreates.com** — 破産寸前のメンテナファンド。

---

## チートシート

```bash
pytest -q
py omega_point.py
py omega_point.py --uri $env:WSS_URI --live
```

ドキュメント: [API リファレンス](../api-reference.md) | [技術アーキテクチャ](../technical-architecture.md)
