from user_id import UserId
from user_name import UserName
from iuser_notification import IUserNotification

class User:
    def __init__(self, id: UserId, name: UserName) -> None:
        if id is None: raise ValueError(f'incorrect value: {id}')
        if name is None: raise ValueError(f'incorrect value: {name}')
        

        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    def change_name(self, name: UserName) -> None:
        if name is None: raise ValueError(f'incorrect value: {name}')

        self._name = name

    def notify(self, note: IUserNotification) -> None:
        note.id = self._id
        note.name = self._name


if __name__ == '__main__':
    user_id = UserId('111-222-333')
    user_name = UserName('tanaka taro')
    user = User(user_id, user_name)

    print(user.id.value, user.name.value)

    print('*'*100)

    user_notification = IUserNotification()
    user.notify(user_notification)

    print(user_notification.id.value, user_notification.name.value)