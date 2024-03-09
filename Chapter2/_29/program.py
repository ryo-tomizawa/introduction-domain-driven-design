from money import Money

class Program:
    def main(self):
        my_money = Money(1000, 'JPY')
        allowance = Money(3000, 'JPY')
        result = my_money.add(allowance)

        # for test
        print(result.amount, result.currency)
    

if __name__ == '__main__':
    program = Program()
    program.main()