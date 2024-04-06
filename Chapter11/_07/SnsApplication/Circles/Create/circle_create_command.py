class CircleApplicationCommand:
    def __init__(self, user_id: str, user_name: str) -> None:
        self._user_id = user_id
        self._user_name = user_name

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def user_name(self):
        return self._user_name
    

if __name__ == '__main__':
    circle_application_command = CircleApplicationCommand('1111', 'sample circle')
    print(circle_application_command.user_id,
          circle_application_command.user_name)