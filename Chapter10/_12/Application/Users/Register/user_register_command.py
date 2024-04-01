class UserRegisterCommand:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name


if __name__ == '__main__':
    user_register_command = UserRegisterCommand('tanaka taro')

    print(
        user_register_command.name,
          )
    