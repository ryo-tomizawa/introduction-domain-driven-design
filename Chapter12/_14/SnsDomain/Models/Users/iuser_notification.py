from user_id import UserId
from user_name import UserName

class IUserNotification:
    def __init__(self) -> None:
        self._id = None
        self._name = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: UserId):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: UserName):
        self._name = name


if __name__ == '__main__':
    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')

    user_notification = IUserNotification()
    user_notification.id = user_id
    user_notification.name = user_name
    print(user_notification.id.value, user_notification.name.value)