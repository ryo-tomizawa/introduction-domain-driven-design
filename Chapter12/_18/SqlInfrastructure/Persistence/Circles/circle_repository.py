import os
import sys

current_dir = os.path.dirname(__file__)
circle_model_dir = os.path.abspath(os.path.join(current_dir, '../../../SnsDomain/Models/Circles'))
sys.path.append(circle_model_dir)

import sqlite3
from circle_id import CircleId
from circle_name import CircleName
from circle import Circle
from icircle_repository import ICircleRepository

class CircleRepository(ICircleRepository):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def save(self, circle: Circle):
        with self.connection:
            query = f"""
                    UPDATE users 
                    SET name = ?
                    WHERE id = ?
                    """
            for user in circle.members:
                self.connection.execute(query, (user.name.value, user.id.value))

        with self.connection:
            query = f"""
                    INSERT INTO circles(
                        id,
                        name,
                        ownerid
                    )
                    values(
                        '{circle.id.value}',
                        '{circle.name.value}',
                        '{circle.owner.id.value}'
                    )
                    on conflict(id)
                    do update
                        set
                        name = '{circle.name.value}',
                        ownerid = '{circle.owner.id.value}'
                    """
            self.connection.execute(query)

        with self.connection:
            query = f"""
                    INSERT INTO userCircles(
                        circleid,
                        userid
                    )
                    values(
                        '{circle.id.value}',
                        ''
                    )
                    on conflict(circleid)
                    do nothing
                    """
            self.connection.execute(query)
    
    def find(self, id: CircleId) -> Circle:
        raise NotImplementedError()
    
    def find_by_user_name(self, name: CircleName) -> Circle:
        raise NotImplementedError()
    

if __name__ == '__main__':
    user_model_dir = os.path.abspath(os.path.join(current_dir, '../../../SnsDomain/Models/Users'))
    sys.path.append(user_model_dir)

    from user_id import UserId
    from user_name import UserName
    from user import User

    connection = sqlite3.connect(':memory:')
    circle_repository = CircleRepository(connection)

    create_query_1 = 'CREATE TABLE users(id text primary key, name text);'
    create_query_2 = 'CREATE TABLE circles(id text primary key, name text, ownerid text);'
    create_query_3 = 'CREATE TABLE userCircles(circleid text primary key, userid text);'

    connection.execute(create_query_1)
    connection.execute(create_query_2)
    connection.execute(create_query_3)

    circle_id = CircleId('1111')
    circle_name = CircleName('sample circle')
    owner = User(UserId('111-222-333'), UserName('tanaka taro'))
    member_1 = User(UserId('userid1'), UserName('username1'))
    circle = Circle(circle_id, circle_name, owner, [member_1])

    circle_repository.save(circle)