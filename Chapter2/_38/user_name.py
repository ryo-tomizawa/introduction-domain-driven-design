class UserName:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'error value: {value}')
        if len(value) < 3: raise ValueError(f'ユーザ名は3文字以上です {value}')

        self.value = value

if __name__ == '__main__':
    user_name = UserName('taro')
    print(user_name.value)