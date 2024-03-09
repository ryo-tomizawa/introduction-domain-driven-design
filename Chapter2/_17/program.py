from full_name import FullName

class Program:
    def main(self):
        name_a = FullName('taro', 'tanaka')
        name_b = FullName('john', 'smith')

        compare_result = name_a == name_b
        print(compare_result)


if __name__ == '__main__':
    program = Program()
    program.main()