from datetime import datetime


class Operation:
    def __init__(
            self,
            state: str,
            date: str,
            amount: str,
            currency_name: str,
            description: str,
            from_: str,
            to: str
    ):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_
        self.state = state
        self.state = state
    def convert_date(self):
        """Функция конвертации даты"""
        iso_date = datetime.fromisoformat(self.date)
        return iso_date.strftime("%d.%m.%Y")

    def mask_payment_info(self, payment_info: str):
        """Функция конвертации счёта"""
        info: list[str] = payment_info.split(" ")
        number_card = info.pop(-1)
        if payment_info.startswitch("Счёт"):
            number_card = number_card + "*"
        else:
            number_card = number_card + "**"
        info.append(number_card)
        return " ".join(info)
