import sqlite3
from typing import Optional

from iuser_repository import IUserRepository
from numbering_api import NumberingApi
from user_id import UserId
from user import User

class UserRepository(IUserRepository):
    def __init__(self, numbering_api: NumberingApi) -> None:
        self.numbering_api = numbering_api

    def save(self, user: User) -> None:
        pass

    def find(self, id: UserId) -> Optional[User]:
        pass

    # 採番処理はリレーショナルデータベースを利用していない
    def next_identity(self) -> UserId:
        response = self.numbering_api.request()
        return UserId(response.next_id())