from userId import UserId
from userName import UserName
from user import User

id_1 = UserId('111')
name_1 = UserName('Tanaka')
user_1 = User(id_1, name_1)

print(User.exists(user_1, user_1))