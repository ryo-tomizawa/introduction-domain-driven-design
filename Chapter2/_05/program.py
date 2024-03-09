from full_name import FullName

class Program:
    def main(self):
        full_name = FullName('taro', 'tanaka')
        print(full_name.last_name)



if __name__ == '__main__':
    program = Program()
    program.main()