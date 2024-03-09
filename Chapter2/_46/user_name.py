class UserName:
    def __init__(self, value: str) -> None:
        if value is None: raise ValueError(f'error value: {value}')
        if len(value) < 3: raise ValueError(f'ユーザ名は3文字以上です {value}')

        self.__value = value

    # for test
    @property
    def user_name(self):
        return self.__value



if __name__ == '__main__':
    user_name = UserName('tanaka taro')
    print(user_name.user_name)