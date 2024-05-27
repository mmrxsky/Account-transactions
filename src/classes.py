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