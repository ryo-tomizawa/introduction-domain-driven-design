class Program:
    def main(self):
        print(0 == 0) # True
        print(0 == 1) # False
        print('a' == 'a') # True
        print('a' == 'b') # False
        print('hello' == 'hello') # True
        print('hello' == 'こんにちは') # False


if __name__ == '__main__':
    program = Program()
    program.main()