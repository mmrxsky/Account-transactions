import json
from pathlib import Path


def load_operations(path: Path) -> list[dict]:
    """ Функция для загрузки данных"""
    with open(path, encoding='utf-8') as operations:
        return json.load(operations)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    """Фильтрация операций классов"""
    return [
        operation
        for operation in operations
        if  ...
    ]


