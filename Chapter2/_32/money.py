from rate import Rate

class Money:
    def __init__(self, amount: int, currency: str) -> None:
        if currency is None: raise ValueError(f'error value: {currency}')

        self.amount = amount
        self.currency = currency

    def add(self, arg: 'Money'):
        if arg is None: raise ValueError(f'error value: {arg}')
        if self.currency != arg.currency: raise ValueError(f'通貨単位が異なります(self: {self.currency}, arg: {arg.currency})')

        return Money(self.amount + arg.amount, self.currency)
    
    def multiply(self, rate: Rate):
        if rate is None: raise ValueError(f'error value: {rate}')

        result = int(self.amount * rate.rate)

        return Money(result, self.currency)


if __name__ == '__main__':
    money = Money(1000, 'JPY')
    rate = Rate(1.05)

    multiple_money = money.multiply(rate)
    print(multiple_money.amount, multiple_money.currency)