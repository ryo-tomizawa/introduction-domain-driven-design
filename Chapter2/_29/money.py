class Money:
    def __init__(self, amount: int, currency: str) -> None:
        if currency is None: raise ValueError(f'error value: {currency}')

        self.amount = amount
        self.currency = currency

    def add(self, arg: 'Money'):
        if arg is None: raise ValueError(f'error value: {arg}')
        if self.currency != arg.currency: raise ValueError(f'通貨単位が異なります(self: {self.currency}, arg: {arg.currency})')

        return Money(self.amount + arg.amount, self.currency)


if __name__ == '__main__':
    money_a = Money(1000, 'JPY')
    print(money_a.amount)
    print(money_a.currency)

    print('*'*100)

    money_b = Money(500, 'JPY')
    print(money_b.amount)
    print(money_b.currency)

    print('*'*100)

    result_money = money_a.add(money_b)
    print(result_money.amount)
    print(result_money.currency)
