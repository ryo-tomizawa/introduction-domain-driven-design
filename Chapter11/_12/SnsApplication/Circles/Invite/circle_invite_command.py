import os
import sys

current_dir = os.path.dirname(__file__)


class CircleInviteCommand:
    def __init__(self, circle_id: str, from_user_id: str, invite_user_id: str) -> None:
        self._circle_id = circle_id
        self._from_user_id = from_user_id
        self._invite_user_id = invite_user_id

    @property
    def circle_id(self):
        return self._circle_id
    
    @property
    def from_user_id(self):
        return self._from_user_id
    
    @property
    def invite_user_id(self):
        return self._invite_user_id
    

if __name__ == '__main__':
    circle_invite_command = CircleInviteCommand('1111', '111-222-333', '444-555-666')
    print(circle_invite_command.circle_id,
          circle_invite_command.from_user_id,
          circle_invite_command.invite_user_id)