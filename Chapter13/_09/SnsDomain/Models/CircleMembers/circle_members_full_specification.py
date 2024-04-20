from circle_members import CircleMembers

class CircleMembersFullSpecification:
    def is_satisfied_by(self, members: CircleMembers):
        premium_user_number = members.count_premium_members(False)
        circle_upper_limit = 30 if premium_user_number < 10 else 50
        return members.count_members() >= circle_upper_limit
    

if __name__ == '__main__':
    import os
    import sys

    current_dir = os.path.dirname(__file__)
    circle_model_dir = os.path.abspath(os.path.join(current_dir, '../Circles'))
    user_model_dir = os.path.abspath(os.path.join(current_dir, '../Users'))

    sys.path.append(circle_model_dir)
    sys.path.append(user_model_dir)

    from circle_id import CircleId
    from user import User
    from user_id import UserId
    from user_name import UserName

    circle_id = CircleId('1111')
    owner = User(UserId('111-222-333'), UserName('tanaka taro'), True)
    member_1 = User(UserId('userid1'), UserName('username1'), True)
    member_2 = User(UserId('userid2'), UserName('username2'), True)
    member_3 = User(UserId('userid3'), UserName('username3'), True)
    member_4 = User(UserId('userid4'), UserName('username4'), True)
    member_5 = User(UserId('userid5'), UserName('username5'), True)
    members = [member_1, member_2, member_3, member_4, member_5]

    circle_members = CircleMembers(circle_id, owner, members)

    circle_members_full_specification = CircleMembersFullSpecification()
    
    print(f'{circle_members_full_specification.is_satisfied_by(circle_members)}')