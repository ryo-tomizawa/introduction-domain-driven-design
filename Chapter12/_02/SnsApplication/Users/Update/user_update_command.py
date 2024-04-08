class UserUpdateCommand:
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
    user_update_command = UserUpdateCommand('111-222-333', 'tanaka taro')

    print(
        user_update_command.id,
        user_update_command.name
          )
    