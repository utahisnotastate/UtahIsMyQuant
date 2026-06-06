# 快速入门 — 10 分钟上手 UtahIsMyQuant

## 前置条件

- Python 3.11+（已测试 3.14）
- Git

## 1. 克隆与安装

```powershell
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. 验证

```bash
pytest -q
```

预期结果：**62 项通过**（约数；请在本地运行以获取精确计数）。

## 3. 运行演示（不涉及真实资金）

| 命令 | 作用 |
|------|------|
| `py omega_point.py` | 闭环回放（tick → alpha → risk） |
| `py main.py` | Omni Discovery + Utahrbitrage 同步 |
| `py main.py --prediction-demo` | Utah Consensus Lattice AMI 演示 |
| `py main.py --dashboard` | Streamlit Omni-Sieve 界面 |

## 4. 下一步阅读

| 目标 | 文档 |
|------|------|
| 理解架构 | [technical-architecture.md](technical-architecture.md) |
| 复制粘贴代码 | [tutorials/README.md](tutorials/README.md) |
| API 查阅 | [api-reference.md](api-reference.md) |
| 从旧栈迁移 | [migration/README.md](migration/README.md) |

## 5. 支持 Utah

若本仓库对你有所帮助：[paying-utah.md](paying-utah.md) — 邮件 [utah@utahcreates.com](mailto:utah@utahcreates.com)。付款 GUI 应用规划中。

## 6. 其他语言

Русский · Eesti · Suomi · 日本語 — 独立页面：[languages.md](languages.md)
