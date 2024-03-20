class HighCohensionA:
    def __init__(self,
                 value3: int,
                 value4: int,
                 ) -> None:
        self.value3 = value3
        self.value4 = value4

    def method_b(self):
        return self.value3 + self.value4
    

if __name__ == '__main__':
    high_cohension = HighCohensionA(3, 4)
    print(f'result of method_a: {high_cohension.method_b()}')