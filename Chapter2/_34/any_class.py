class AnyClass:
    def method(self, model_number: str):
        print(model_number)


if __name__ == '__main__':
    program = AnyClass()
    program.method('aa-bb-cc-dd')