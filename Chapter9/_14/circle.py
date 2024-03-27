from circle_name import CircleName
from user_id import UserId

class Circle:
    def __init__(self, owner_id: UserId, name: CircleName) -> None:
        if owner_id is None: raise ValueError(f'incorrect value: {owner_id}')
        if name is None: raise ValueError(f'incorrect value: {name}')

        self._owner_id = owner_id
        self._name = name

    @property
    def owner_id(self):
        return self._owner_id
    
    @property
    def name(self):
        return self._name
    


if __name__ == '__main__':
    owner_id = UserId('111-222-333')
    circle_name = CircleName('sample circle name')

    circle = Circle(owner_id, circle_name)

    print(circle.owner_id.value, circle.name.value)