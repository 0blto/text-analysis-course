# Лабораторная работа №2

В `notebook.ipynb` разобраны морфология и части речи в форумных репликах RuHateBe, распределение частей речи по классам, ошибки модели, деревья зависимостей, пары «подлежащее + действие» и анафора.

## Запуск

Из каталога `lab2`:

```bash
uv sync --locked
uv run python -m ipykernel install --sys-prefix --name lab2 --display-name "Python (lab2)"
uv run jupyter notebook notebook.ipynb
```

Сервер и ядро используют `lab2/.venv`. В Jupyter ядро отображается как **Python (lab2)**. Датасет общий для обеих работ и читается из `../data/balanced_RUHABE.csv`.

Для анализа берём `Reply 2 original`, а для анафоры используем и предыдущую реплику `Reply 1 original`. Классы `target_group` обозначают объект агрессии. Варианты `migrant` и `migrants` объединены для сравнения. Повторные реплики сохранены.

Ноутбук при запуске заново разбирает корпус. В `results/` лежат файлы разбора с более раннего запуска.
