class User:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name


if __name__ == '__main__':
    user = User('tanaka taro')
    print(user.name)

    print('*'*100)
    user.name = 'john smith'

    print(user.name)