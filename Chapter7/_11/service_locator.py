class ServiceLocator:
    def __init__(self) -> None:
        self._map = {}

    def resolve(self, type: str):
        if type in self._map:
            return self._map[type]
        else:
            return None
    
    def register(self, type: str, obj: object):
        self._map[type] = obj


if __name__ == '__main__':
    class MockClass:
        def __init__(self) -> None:
            self.name = 'MyClass Instance'

    service_locator = ServiceLocator()
    service_locator.register('MyClass', MockClass())

    instance = service_locator.resolve('MyClass')

    print(instance.name)