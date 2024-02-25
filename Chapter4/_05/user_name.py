class UserName:
    def __init__(self, value: str) -> None:
        if value is None:
            raise ValueError(f'incorrect value: {value}')
        if len(value) < 3:
            raise ValueError(f'ユーザ名は３文字以上です。 {value}')
        self.value = value