from user_id import UserId

class User:
    def __init__(self, id: UserId, name: str) -> None:
        if id is None: raise ValueError(f'error value: {id}')
        if name is None or len(name) == 0: raise ValueError(f'error value: {name}')

        self.id = id
        self.name = name


if __name__ == '__main__':
    user_id = UserId('1-1-1')
    user = User(user_id, 'tanaka taro')

    print(user.id.value, user.name)