class Program:
    def main(self):
        user_name = 'me'
        
        if len(user_name) >= 3:
            print(f'Hello {user_name}')
        else:
            print(f'Invalid user name.')

if __name__ == '__main__':
    program = Program()
    program.main()