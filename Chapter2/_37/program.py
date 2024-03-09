class Program:
    def main(self):
        user_name = 'me'
        
        if len(user_name) >= 3:
            # 正常な値なので処理を継続する
            pass
        else:
            raise ValueError(f'異常な値です')

if __name__ == '__main__':
    program = Program()
    program.main()