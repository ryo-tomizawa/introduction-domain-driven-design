class Program:
    def main(self):
        'こんにちは'.change_to('Hello') # このようなメソッドは本来存在しない
        print('こんにちは') # Helloが表示される


if __name__ == '__main__':
    program = Program()
    program.main()