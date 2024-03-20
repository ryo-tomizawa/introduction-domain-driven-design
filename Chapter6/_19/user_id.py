class UserId:
    def __init__(self, value: str) -> None:
        if value is None or len(value) == 0: raise ValueError(f'valueがnullまたは空文字です')
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
    user_id_a = UserId('1010')
    print(user_id_a.value)

    print('*'*100)

    user_id_b = UserId('2222')
    print(user_id_a == user_id_b)