class UserUpdateCommand:
    def __init__(self, id: str) -> None:
        self._id = id
        self._name = None
        self._mail_address = None

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mail_address(self):
        return self._mail_address
    
    @mail_address.setter
    def mail_address(self, value):
        self._mail_address = value


if __name__ == '__main__':
    user_update_command = UserUpdateCommand('111-222-333')
    user_update_command.name = 'tanaka taro'
    user_update_command.mail_address = 'test@example.com'

    print(
        user_update_command.id,
        user_update_command.name,
        user_update_command.mail_address
          )
    