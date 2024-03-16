from user_id import UserId

class User:
    def __init__(self, id: UserId, name: str) -> None:
        if id is None: raise ValueError(f'error value: {id}')

        self._id = id
        self.change_user_name(name)

    def change_user_name(self, name:str):
        if name is None or len(name) == 0: raise ValueError(f'error value: {name}')
        if len(name) < 3: raise ValueError(f'ユーザ名は3文字以上です {name}')
        self.name = name

    def __eq__(self, other: 'User'):
        if other is None: return False
        if id(self) == id(other): return True
        if type(self) != type(other): return False

        return self._id.value == other._id.value


if __name__ == '__main__':
    user_a = User(UserId('1-1-1'), 'tanaka taro')
    user_b = User(UserId('1-1-1'), 'tanaka taro')
    user_c = User(UserId('2-2-2'), 'john smith')

    print(user_a == user_b)
    print('*'*100)
    print(user_a == user_c)