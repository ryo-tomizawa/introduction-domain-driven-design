from first_name import FirstName
from last_name import LastName

import re

class FullName:
    def __init__(self, first_name: FirstName, last_name: LastName) -> None:
        # NULL check
        if first_name is None or len(first_name._value) == 0: raise ValueError(f'error of first_name: {first_name}')
        if last_name is None or len(last_name._value) == 0: raise ValueError(f'error of last_name: {last_name}')

        # validate check
        if not self.validate_name(first_name._value): raise ValueError(f'許可されていない文字列が使われています: {first_name}')
        if not self.validate_name(last_name._value): raise ValueError(f'許可されていない文字列が使われています: {last_name}')

        self._first_name = first_name
        self._last_name = last_name

    def validate_name(self, value: str) -> bool:
        return bool(re.match("^[A-Za-z]+$", value))

    def __eq__(self, other) -> bool:
        if other is None: return False
        if id(self) == id(other): return True
        if type(self) != type(other): return False

        return self._first_name._value == other._first_name._value and \
                self._last_name._value == other._last_name._value


if __name__ == '__main__':
    name_a = FullName(FirstName('taro'), LastName('tanaka'))
    name_b = FullName(FirstName('taro'), LastName('tanaka'))
    name_c = FullName(FirstName('john'), LastName('smith'))

    print(name_a == name_b)
    print('*'*100)
    print(name_a == name_c)