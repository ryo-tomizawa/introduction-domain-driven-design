class CircleUpdateCommand:
    def __init__(self, id: str, name: str) -> None:
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    

if __name__ == '__main__':
    circle_update_command = CircleUpdateCommand('1111', 'sample circle')
    print(circle_update_command.id,
          circle_update_command.name)