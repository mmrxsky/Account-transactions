from config import OPERATION_PATH
from src.utils import load_operations, get_operation_instances, sort_operations


def main():
    operations = load_operations(OPERATION_PATH)
    operations = operations[:5]
    operation_instances = get_operation_instances(operations)
    sorted_operations = sort_operations(operation_instances)
    for operation in operation_instances:
        print()
        print(operation)


if __name__ == '__main__':
    main()