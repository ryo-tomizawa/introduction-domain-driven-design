class User:
    def __init__(self, name: str) -> None:
        self.change_name(name)

    def change_name(self, name: str):
        if name is None or len(name) == 0: raise ValueError(f'error value: {name}')
        if len(name) < 3: raise ValueError(f'ユーザ名は3文字以上です {name}')
        self.name = name



if __name__ == '__main__':
    user = User('tanaka taro')
    print(user.name)