from user_name import UserName

class User:
    def __init__(self, name: UserName) -> None:
        if name is None or len(name.user_name) == 0: raise ValueError(f'error value: {name.user_name}')
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value



if __name__ == '__main__':
    user = User(UserName('tanaka taro'))
    print(user.name.user_name)