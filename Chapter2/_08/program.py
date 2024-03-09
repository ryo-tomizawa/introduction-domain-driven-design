class Program:
    def main(self):
        greet = 'こんにちは'
        # greet.change_to('Hello') #このようなメソッドは本来存在しない
        print(greet) # Helloが表示される


if __name__ == '__main__':
    program = Program()
    program.main()