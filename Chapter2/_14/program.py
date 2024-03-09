from full_name import FullName

class Program:
    def main(self):
        name_a = FullName('taro', 'tanaka')
        name_b = FullName('taro', 'tanaka')

        print(name_a == name_b)


if __name__ == '__main__':
    program = Program()
    program.main()