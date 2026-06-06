# 教程 01：安装与验证

## 目标

克隆 UtahIsMyQuant，安装依赖，确认全部测试通过。

## 步骤

### 1. 克隆

```bash
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
```

### 2. 虚拟环境

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. 运行测试

```bash
pytest -q
```

### 4. 探索布局

```text
src/           Core engines
tests/         62+ unit tests
omega_point.py Closed-loop runner
main.py        Omni + prediction demos
docs/          All documentation
examples/      Runnable example scripts
```

### 5. 首次演示

```bash
py omega_point.py
```

应看到以 `// OMEGA COMPLETE` 结尾的日志行。

## 故障排除

| 问题 | 修复 |
|------|------|
| 找不到 `python` | Windows 上使用 `py` |
| `websockets` 导入错误 | `pip install -r requirements.txt` |
| 测试挂起 | 确保无僵尸 Python；`pytest -q --maxfail=1` |

## 下一步

[教程 02：首个回放流水线](02-first-replay-pipeline.md)
