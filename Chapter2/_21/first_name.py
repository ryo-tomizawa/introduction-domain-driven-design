class FirstName:
    def __init__(self, value: str) -> None:
        if value is None or len(value) == 0: raise ValueError(f'1文字以上である必要があります。 {value}')
        self._value = value


if __name__ == '__main__':
    first_name = FirstName('taro')
    print(first_name._value)