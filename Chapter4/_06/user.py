from user_id import UserId
from user_name import UserName

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        self._id = id
        self.name = name