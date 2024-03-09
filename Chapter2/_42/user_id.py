class UserId:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'error value: {value}')

        self.value = value

if __name__ == '__main__':
    user_id = UserId('1-2-3-4-5')
    print(user_id.value)