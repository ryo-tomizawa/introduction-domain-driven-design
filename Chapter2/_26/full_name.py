from name import Name

import re

class FullName:
    def __init__(self, first_name: Name, last_name: Name) -> None:
        # NULL check
        if first_name is None or len(first_name._value) == 0: raise ValueError(f'error of first_name: {first_name}')
        if last_name is None or len(last_name._value) == 0: raise ValueError(f'error of last_name: {last_name}')

        self._first_name = first_name
        self._last_name = last_name


if __name__ == '__main__':
    name = FullName(Name('taro'), Name('tanaka'))

    print(name._first_name._value)
    print(name._last_name._value)