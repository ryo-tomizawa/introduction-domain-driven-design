class CircleId:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'incorrect value: {value}')
        self._value = value

    @property
    def value(self):
        return self._value
    

if __name__ == '__main__':
    circle_id = CircleId('111-222-333')
    print(circle_id.value)