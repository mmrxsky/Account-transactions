import pytest
from src.classes import Operation


@pytest.fixture
def operation():
    return Operation(
            state ="EXECUTED",
            from_ =None,
            date ="2019-07-03T18:35:29.512364",
            amount ="8221.37",
            currency_name ="USD",
            description ="Перевод организации",
            to ="Счет 11776614605963066702"
    )



@pytest.fixture
def operations():
    return [
        Operation(
            state = "EXECUTED",
            from_ = None,
            date = "2019-07-03T18:35:29.512364",
            amount = "8221.37",
            currency_name = "USD",
            description = "Перевод организации",
            to = "Счет 11776614605963066702"
    ),
        Operation(
            state="EXECUTED",
            from_=None,
            date="2018-06-30T02:08:58.425572",
            amount="9824.07",
            currency_name="USD",
            description="Перевод организации",
            to="Счет 11776614605963066702"
        ),
        Operation(
            state="EXECUTED",
            from_=None,
            date="2019-04-04T23:20:05.206878",
            amount="79114.93",
            currency_name="USD",
            description="Перевод организации",
            to="Счет 11776614605963066702"
        ),
    ]
