# チュートリアル 08: ライブ WebSocket フィード

## 目標

実際の `wss://` ティックフィードを Sentinel オブザーバーに接続する。

## 前提条件

- データベンダーの WebSocket URL
- `websockets` インストール済み

## 実行

```bash
py omega_point.py --uri wss://YOUR_FEED_URL --live
```

または:

```bash
py main.py --uri wss://YOUR_FEED_URL --live
```

## JSON を正規化

必要なら `Tick.from_payload` を拡張:

```python
# src/tick_observer.py — add keys your vendor uses
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

## 安全

1. 拒否挙動を検証するまで **ペーパートレードのみ**
2. すべての `EXECUTE_*` をファイルにログ
3. ネットワークに合った `max_latency_ms` を設定

## 次へ

[チュートリアル 09: カスタムブローカーアダプター](09-custom-broker-adapter.md)
