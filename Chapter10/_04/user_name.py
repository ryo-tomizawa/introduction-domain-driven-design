class UserName:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'incorrect value: {value}')
        if len(value) < 3: raise ValueError(f'ユーザ名は３文字以上です: {value}')
        if len(value) > 20: raise ValueError(f'ユーザ名は20文字以下です: {value}')
        self._value = value

    @property
    def value(self):
        return self._value
    
    def __eq__(self, __value: object) -> bool:
        if __value is None: return False
        if id(self) == id(__value): return True
        if type(self) != type(__value): return False

        return self.value == __value.value



if __name__ == '__main__':
    user_name_a = UserName('tanaka taro')
    print(user_name_a.value)

    print('*'*100)

    user_name_b = UserName('tanaka taro')
    print(user_name_a == user_name_b)

    print('*'*100)
    user_name_c = UserName('john smith')
    print(user_name_a == user_name_c)