class Program:
    def main(self):
        full_name = 'john smith'
        tokens = full_name.split(' ')
        last_name = tokens[0]
        print(last_name)



if __name__ == '__main__':
    program = Program()
    program.main()