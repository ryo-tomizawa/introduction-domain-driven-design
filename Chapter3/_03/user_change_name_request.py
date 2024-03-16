class UserChangeNameRequest:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value