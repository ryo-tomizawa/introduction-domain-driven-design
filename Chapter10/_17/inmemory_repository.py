from typing import TypeVar, Generic, Dict, Hashable

TKey = TypeVar('TKey', bound=Hashable)
TEntity = TypeVar('TEntity')

class InMemoryRepository(Generic[TKey, TEntity]):
    def __init__(self):
        self.creates: Dict[TKey, TEntity] = {}
        self.updates: Dict[TKey, TEntity] = {}
        self.deletes: Dict[TKey, TEntity] = {}
        self.db: Dict[TKey, TEntity] = {}

    @property
    def data(self) -> Dict[TKey, TEntity]:
        data_dict = {**self.db, **self.creates, **self.updates}
        
        if self.deletes:
            for k in self.deletes.keys():
                del data_dict[k]
        return data_dict

    def save(self, entity: TEntity):
        id = self.get_id(entity)
        target_map = self.updates if id in self.data else self.creates
        target_map[id] = self.clone(entity)

    def remove(self, entity: TEntity):
        id = self.get_id(entity)
        self.deletes[id] = self.clone(entity)

    def commit(self):
        self.db = self.data
        self.creates.clear()
        self.updates.clear()
        self.deletes.clear()

    def get_id(self, entity: TEntity) -> TKey:
        raise NotImplementedError

    def clone(self, entity: TEntity) -> TEntity:
        raise NotImplementedError
    
if __name__ == '__main__':
    class User:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    class UserRepository(InMemoryRepository[str, User]):
        def get_id(self, entity):
            return entity.id

        def clone(self, entity):
            return User(entity.id, entity.name)

    # Create an instance of UserRepository
    user_repository = UserRepository()

    user1 = User('111-222-333', 'tanaka taro')
    user2 = User('222-333-444', 'john smith')

    # Save users
    user_repository.save(user1)
    user_repository.save(user2)

    # Remove a user
    user_repository.remove(user1)

    # Commit changes
    user_repository.commit()

    # Display all users
    all_users = user_repository.data.values()
    for user in all_users:
        print(f"User ID: {user.id}, Name: {user.name}")