from money import Money

class Program:
    def main(self):
        jpy = Money(1000, 'JPY')
        usd = Money(3000, 'USD')
        result = jpy.add(usd) # 例外が出力される

        # for test
        print(result.amount, result.currency)
    

if __name__ == '__main__':
    program = Program()
    program.main()