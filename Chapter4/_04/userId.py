class UserId:
    def __init__(self, value: str) -> None:
        if value is None:
            raise ValueError(f'incorrect value: {value}')
        self.value = value