class UserId:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'incorrect value: {value}')
        self.value = value


if __name__ == '__main__':
    user_id = UserId('1010')
    print(user_id.value)