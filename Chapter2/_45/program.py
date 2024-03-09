from user import User

class Program:
    def create_user(self, name: str):
        if name is None: raise ValueError(f'error value: {name}')
        if len(name) < 3: raise ValueError(f'ユーザ名は3文字以上です {name}')
        
        user = User(name)
        # ...

    def update_user(self, id: str, name: str):
        if name is None: raise ValueError(f'error value: {name}')
        if len(name) < 3: raise ValueError(f'ユーザ名は3文字以上です {name}')

        # ...  


if __name__ == '__main__':
    program = Program()
    user = program.create_user('tanaka taro')