from circle_invitation import CircleInvitation

class ICircleInvitationRepository:
    def save(self, circle_invitation: CircleInvitation):
        pass


if __name__ == '__main__':
    import os
    import sys

    current_dir = os.path.dirname(__file__)
    circle_model_dir = os.path.abspath(os.path.join(current_dir, '../Circles'))
    user_model_dir = os.path.abspath(os.path.join(current_dir, '../Users'))

    sys.path.append(circle_model_dir)
    sys.path.append(user_model_dir)

    from circle import Circle
    from circle_id import CircleId
    from circle_name import CircleName
    from user import User
    from user_id import UserId
    from user_name import UserName
    
    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member = User(UserId('222-333-444'), UserName('john smith'))
    members =[member]

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')
    circle = Circle(circle_id, circle_name, owner, members)

    invite_user = User(UserId('333-444-555'), UserName('james bond'))
    circle_invitation = CircleInvitation(circle, owner, invite_user)

    circle_invitation_repository = ICircleInvitationRepository()
    print(circle_invitation_repository.save(circle_invitation))