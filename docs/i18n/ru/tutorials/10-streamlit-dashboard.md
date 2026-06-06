# Учебник 10: Streamlit dashboard

## Цель

Запустить **Omni-Sieve** dashboard для сравнения VaR proxy и symplectic capacity.

## Запуск

```bash
pip install streamlit
py main.py --dashboard
```

Или:

```bash
streamlit run src/ui/omni_sieve_dashboard.py
```

## Что вы увидите

- Слева: синтетический прокси дисперсии «incumbent»  
- По центру: symplectic manifold capacity  
- Справа: последний resonance utah-flux  

## Настройка

Отредактируйте `src/ui/omni_sieve_dashboard.py`, чтобы подключить live flux stream.

## Готово

Вернитесь к [индексу учебников](README.md) или [полному индексу документации](../README.md).
