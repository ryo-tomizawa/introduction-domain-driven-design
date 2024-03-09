from first_name import FirstName
from last_name import LastName

class FullName:
    def __init__(self, first_name: FirstName, last_name: LastName) -> None:
        self._first_name = first_name
        self._last_name = last_name

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