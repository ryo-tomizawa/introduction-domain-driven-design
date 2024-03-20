class HighCohensionA:
    def __init__(self,
                 value1: int,
                 value2: int,
                 ) -> None:
        self.value1 = value1
        self.value2 = value2

    def method_a(self):
        return self.value1 + self.value2
    

if __name__ == '__main__':
    high_cohension = HighCohensionA(1, 2)
    print(f'result of method_a: {high_cohension.method_a()}')