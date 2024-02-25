from userId import UserId
from userName import UserName
from user import User

check_id = UserId('check')
check_name = UserName('checker')

id = UserId('id')
name = UserName('nrs')

check_user = User(check_id, check_name)
user = User(id, name)
print(User.exists(check_user, user))