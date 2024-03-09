class User:
    def __init__(self, name: str) -> None:
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value



if __name__ == '__main__':
    user = User('tanaka taro')
    print(user.name)