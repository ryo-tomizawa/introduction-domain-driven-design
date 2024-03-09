class FullName:
    def __init__(self, first_name: str, middle_name: str, last_name: str) -> None:
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def middle_name(self):
        return self._middle_name

    @property
    def last_name(self):
        return self._last_name
    
    def __eq__(self, other) -> bool:
        if other is None: return False
        if id(self) == id(other): return True
        if type(self) != type(other): return False
        return self._first_name == other._first_name and \
                self._middle_name == other._middle_name and \
                self._last_name == other._last_name
    
    def __hash__(self):
        return hash((self._first_name, self._last_name))
        

if __name__ == '__main__':
    full_name = FullName('taro', 'edward', 'tanaka')
    print(full_name.first_name)
    print(full_name.middle_name)
    print(full_name.last_name)