from full_name import FullName

class Program:
    def main(self):
        full_name = FullName('taro', 'tanaka')
        full_name.change_last_name('kato')


if __name__ == '__main__':
    program = Program()
    program.main()