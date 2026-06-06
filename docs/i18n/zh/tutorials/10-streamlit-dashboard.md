# 教程 10：Streamlit 仪表盘

## 目标

启动 **Omni-Sieve** 仪表盘，并排查看 VaR 代理与辛容量。

## 运行

```bash
pip install streamlit
py main.py --dashboard
```

或：

```bash
streamlit run src/ui/omni_sieve_dashboard.py
```

## 你将看到

- 左：合成「既有」方差代理
- 中：辛流形容量
- 右：utah-flux 最新共振

## 自定义

编辑 `src/ui/omni_sieve_dashboard.py` 以接入你的实时 flux 流。

## 完成

返回 [教程 README](README.md) 或 [完整文档索引](../README.md)。
