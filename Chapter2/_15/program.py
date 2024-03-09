from full_name import FullName

class Program:
    def main(self):
        name_a = FullName('taro', 'tanaka')
        name_b = FullName('john', 'smith')

        compare_result = name_a._first_name == name_b._first_name and \
            name_a.last_name == name_b._last_name
        
        print(compare_result)


if __name__ == '__main__':
    program = Program()
    program.main()