from user import User
from user_change_name_request import UserChangeNameRequest

class MyProgram:
    def main(self, user: User, request: UserChangeNameRequest):
        if request is None or len(request.name) == 0:
            raise ValueError('リクエストのNameがnullまたは空です')
    
        user.change_name(request.name)


if __name__ == '__main__':
    user_a = User('tanaka taro')
    request_name = UserChangeNameRequest('john smith')

    user_a.change_name(request_name.name)

    print(user_a.name)