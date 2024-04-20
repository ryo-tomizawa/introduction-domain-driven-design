from circle_id import CircleId

class CircleFullException(Exception):
    def __init__(self, id: CircleId, message: str = '') -> None:
        super().__init__(message)
        self._id = id

    @property
    def id(self):
        return self._id
    

if __name__ == '__main__':
    circle_id = CircleId('1111')

    try:
        raise CircleFullException(circle_id, 'can not found circle ID')
    except CircleFullException as e:
        print(f'Error: {e}')
        print(f'Circle ID: {e.id.value}')