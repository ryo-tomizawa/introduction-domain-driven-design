class LastName:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'1文字以上である必要があります。 {value}')
        self._value = value


if __name__ == '__main__':
    first_name = LastName('tanaka')
    print(first_name._value)