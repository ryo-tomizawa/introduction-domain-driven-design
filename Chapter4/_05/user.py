from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        if id is None:
            raise ValueError(f'incorrect UserId: {id}')
        if name is None:
            raise ValueError(f'incorrect UserName: {name}')
        self._id = id
        self.name = name