class CircleJoinCommand:
    def __init__(self, user_id: str, circle_id: str) -> None:
        self._user_id = user_id
        self._circle_id = circle_id

    @property
    def user_id(self):
        return self._user_id
    
    @property
    def circle_id(self):
        return self._circle_id
    

if __name__ == '__main__':
    circle_join_command = CircleJoinCommand('111-222-333', '1111')
    print(circle_join_command.user_id,
          circle_join_command.circle_id)