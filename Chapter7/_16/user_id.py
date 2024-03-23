class UserId:
    def __init__(self, value: str) -> None:
        if value is None or len(value) == 0: raise ValueError(f'valueがnullまたは空文字です')
        self._value = value

    @property
    def value(self):
        return self._value


if __name__ == '__main__':
    user_id_a = UserId('1010')
    print(user_id_a.value)