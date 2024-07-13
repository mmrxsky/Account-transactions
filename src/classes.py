from datetime import datetime


class Operation:
    def __init__(
            self,
            state: str,
            date: str,
            amount: str,
            currency_name: str,
            description: str,
            from_: str | None,
            to: str
    ):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_ if from_ is not None else ""
        self.to = to

    def convert_date(self):
        """Функция конвертации даты"""
        iso_date = datetime.fromisoformat(self.date)
        return iso_date.strftime("%d.%m.%Y")

    def mask_payment_info(self, payment_info: str):
        """Функция конвертации счёта"""
        info: list[str] = payment_info.split(" ")
        number_card = info.pop(-1)
        if payment_info.startswith("Счёт"):
            number_card = number_card + "*"
        else:
            number_card = number_card + "**"
        info.append(number_card)
        return " ".join(info)


    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date

    def __str__(self):
        from_ = self.mask_payment_info(self.from_)
        delimiter = " -> " if from_ else ""
        return (
            f"{self.convert_date()} {self.description}\n"
            f"{self.mask_payment_info(self.from_)} -> {self.mask_payment_info(self.to)}\n"
            f"{self.amount} {self.currency_name}"
        )
