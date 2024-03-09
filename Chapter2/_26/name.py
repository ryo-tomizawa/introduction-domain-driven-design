import re

class Name:
    def __init__(self, value: str) -> None:
        if value is None or len(value) == 0: raise ValueError(f'error of name: {value}')
        if not bool(re.match("^[A-Za-z]+$", value)): raise ValueError(f'許可されていない文字列が使われています: {value}')
        self._value = value


if __name__ == '__main__':
    name = Name('taro')
    print(name._value)