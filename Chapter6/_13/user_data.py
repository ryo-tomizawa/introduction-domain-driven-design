from user import User

class UserData:
    def __init__(self, user: User) -> None:
        self._id = user.id.value
        self._name = user.name.value
        self._mail_address = user.mail_address.value # 属性への第集処理

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    # 追加された属性
    @property
    def mail_address(self):
        return self._mail_address


if __name__ == '__main__':
    from user_id import UserId
    from user_name import UserName
    from mail_address import MailAddress

    user = User(UserId('111-222-333'), UserName('tanaka taro'), MailAddress('test@example.com'))
    user_data = UserData(user)

    print(user_data.id, user_data.name, user_data.mail_address)