from userId import UserId
from userName import UserName

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        if id is None:
            raise ValueError(f'incorrect UserId: {id}')
        if name is None:
            raise ValueError(f'incorrect UserName: {name}')
        self._id = id
        self.name = name

    @classmethod
    def exists(cls, user_left: 'User', user_right: 'User') -> bool:
        return user_left._id.value == user_right._id.value and user_left.name.value == user_right.name.value