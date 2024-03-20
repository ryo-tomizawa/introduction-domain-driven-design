class UserUpdateCommand:
    def __init__(self, id: str) -> None:
        self._id = id
        self._name = None
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


if __name__ == '__main__':
    user_update_command = UserUpdateCommand('111-222-333')
    user_update_command.name = 'tanaka taro'

    print(
        user_update_command.id,
        user_update_command.name
          )
    