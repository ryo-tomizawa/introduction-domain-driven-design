class UserId:
    def __init__(self, value: str) -> None:
        if value is None or len(value) == 0: raise ValueError(f'error value: {value}')
        self.value = value


if __name__ == '__main__':
    user_id = UserId('1-1-1')
    print(user_id.value)