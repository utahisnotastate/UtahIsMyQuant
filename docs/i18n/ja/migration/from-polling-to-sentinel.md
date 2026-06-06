# 移行: ポーリング / REST → Sentinel（WebSocket）

## 該当する場合…

- `requests.get()`、cron、1–5秒ポーリングで価格が届く
- デスクの「リアルタイム」は「株式向けに十分速い更新」
- MDH チームが同じ REST エンドポイントを呼ぶ Python スクリプト40本を所有

## 何が変わるか

| 以前 | 以後 |
|--------|-------|
| 間隔でプル | ティックでプッシュ（`websockets`） |
| ホットパスでブロッキング I/O | `asyncio` キューがネットワークとロジックを分離 |
| 遅延 = ポール周期 + RTT | 遅延 = 処理のみ（`latency_us` 参照） |

## 切り替え手順

### 1. フィード形式をミラー

ベンダー JSON を `Tick.from_payload` にマップ:

```python
# Vendor: {"ticker": "SPY", "last": 450.12, "size": 100}
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

または `tick_observer.py` の `from_payload` にキーを追加。

### 2. ポーリング横で sentinel を立てる（週1–2）

```python
observer = TickObserver(uri="wss://vendor/stream")
observer.subscribe(log_only_handler)  # no execution
observer.start_sentinel()
```

レガシーポーラーを継続；タイムスタンプと最終価格を比較。

### 3. 遅いデータ税を測定

ティックごとに `TickObserver.latency_us(tick)` をログ。負荷下で p99 > 200ms ならスーパーバイザーがサーキットブレーカー — **意図的**。

### 4. ポーラーを廃止（週3+）

- 本番ロジックを `observer.ingest` または WebSocket のみに
- cron を廃止；EOD 照合用バッチ1本のみ残す

## 落とし穴

| 落とし穴 | 対処 |
|---------|-----|
| WebSocket 再接続嵐 | `listen()` を指数バックオフでラップ（アダプター側） |
| 部分メッセージ | `queue.put` 前に JSON 検証 |
| シンボルマッピングずれ | シンボロジテーブルを一元化 |
| レガシー同期アプリ内の asyncio | 専用プロセスでループ実行（OmegaPoint パターン） |

## ロールバック計画

30日間ポーラーを読み取り専用で維持。sentinel 失敗時はポーラーログにフォールバック — サイレント失敗しない。

## 次へ

- [バックテスト偏重 → リアルタイム](from-backtest-heavy-to-realtime.md)
- [技術アーキテクチャ](../technical-architecture.md)
