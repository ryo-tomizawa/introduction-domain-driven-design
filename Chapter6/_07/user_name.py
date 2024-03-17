class UserName:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'incorrect value: {value}')
        if len(value) < 3: raise ValueError(f'ユーザ名は３文字以上です: {value}')
        if len(value) > 20: raise ValueError(f'ユーザ名は20文字以下です: {value}')
        self._value = value

    @property
    def value(self):
        return self._value



if __name__ == '__main__':
    user_name = UserName('tanaka taro')
    print(user_name.value)