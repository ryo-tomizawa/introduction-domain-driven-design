class Rate:
    def __init__(self, value: float) -> None:
        self.value = value
    
    @property
    def rate(self):
        return self.value


if __name__ == '__main__':
    rate = Rate(1.05)
    print(rate.rate)