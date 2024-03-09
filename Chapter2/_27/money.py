class Money:
    def __init__(self, amount: int, currency: str) -> None:
        if currency is None: raise ValueError(f'error value: {currency}')

        self.amount = amount
        self.currency = currency


if __name__ == '__main__':
    money = Money(1000, 'JPY')
    print(money.amount)
    print(money.currency)