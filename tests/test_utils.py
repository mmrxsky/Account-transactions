from src.classes import Operation
from src.utils import get_executed_operations, sort_operations


def test_get_executed_operations():
    data = [
        {
            1:1
        },
        {
            2:2
        },
        {},
        {
            3:3
        },
    ]

    expected_operations =[
        {
            1: 1
        },
        {
            2: 2
        },
        {
            3: 3
        },
    ]

    executed_operations = get_executed_operations(data)
    assert executed_operations == executed_operations
    assert len(executed_operations) == 3


def test_sort_operations(operations):
    sorted_operations = sort_operations(operations)
    assert isinstance(sorted_operations, list)
    assert len(sorted_operations) > 0
    assert isinstance(sorted_operations[0], Operation)

