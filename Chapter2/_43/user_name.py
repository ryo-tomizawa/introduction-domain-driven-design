class UserName:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'error value: {value}')

        self.value = value

if __name__ == '__main__':
    user_name = UserName('taro')
    print(user_name.value)