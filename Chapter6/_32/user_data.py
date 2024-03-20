class UserData:
    def __init__(self, id: str, name: str) -> None:
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    


if __name__ == '__main__':
    user_data = UserData('111-222-333', 'tanaka taro')

    print(user_data.id, user_data.name)