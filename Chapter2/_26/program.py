from full_name import FullName
from name import Name

class Program:
    def main(self):
        first_name = Name('taro')
        last_name = Name('tanaka')
        name = FullName(first_name, last_name)

        # for test
        print(name._first_name._value)
        print(name._last_name._value)


if __name__ == '__main__':
    program = Program()
    program.main()