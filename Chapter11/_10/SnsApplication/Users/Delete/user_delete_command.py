class UserDeleteCommand:
    def __init__(self, id: str) -> None:
        self._id = id

    @property
    def id(self):
        return self._id


if __name__ == '__main__':
    user_delete_command = UserDeleteCommand('111-222-333')

    print(
        user_delete_command.id,
          )
    