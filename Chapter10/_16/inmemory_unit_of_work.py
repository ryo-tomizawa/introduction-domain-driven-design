from Domain.Shared.iunit_of_work import IUnitOfWork
from inmemory_user_repository import InMemoryUserRepository

class InMemoryUnitOfWork(IUnitOfWork):
    def __init__(self) -> None:
        self._user_repository = InMemoryUserRepository()

    @property
    def user_repository(self):
        return self._user_repository
    
    def commit(self):
        self.user_repository.commit()