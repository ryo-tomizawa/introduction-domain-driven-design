class LowCohension:
    def __init__(self,
                 value1: int,
                 value2: int,
                 value3: int,
                 value4: int
                 ) -> None:
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4

    def method_a(self):
        return self.value1 + self.value2
    
    def method_b(self):
        return self.value3 + self.value4
    

if __name__ == '__main__':
    low_cohension = LowCohension(1, 2, 3, 4)
    print(f'result of method_a: {low_cohension.method_a()}')
    print(f'result of method_b: {low_cohension.method_b()}')