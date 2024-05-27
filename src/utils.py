import json
from pathlib import Path

from src.classes import Operation


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


def get_operation_instances(operations: list[dict]) -> list[Operation]:
    """Функция раскладывает все операции в экземпляры классов"""
    operation_instances = []
    for operation in operations:
        operation_instance = Operation(
            state=operation["state"],
            from_=operation.get["from"],
            date=operation["date"],
            amount=operation["operationAmount"]["amount"],
            currency_name=operation["operationAmount"],
            description=operation["description"],
            to=operation["to"],
        )
        operation_instances.append(operation_instance)
    return operation_instances

def sort_operations(operations: list[Operation]) -> list[Operation]:
    """Функция сортировка операций"""
    return sorted(operations, reverse=True)
