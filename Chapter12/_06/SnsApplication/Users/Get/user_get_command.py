class UserGetCommand:
    def __init__(self, id: str) -> None:
        self._id = id

    @property
    def id(self):
        return self._id


if __name__ == '__main__':
    user_get_command = UserGetCommand('111-222-333')

    print(
        user_get_command.id,
          )
    