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


if __name__ == '__main__':
    user_id = UserId('1-1-1')
    user = User(user_id, 'tanaka taro')

    print(user._id.value, user.name)