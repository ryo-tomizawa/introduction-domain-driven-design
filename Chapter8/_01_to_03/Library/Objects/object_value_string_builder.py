class ObjectValueStringBuilder:
    def __init__(self, key=None, value=None) -> None:
        self._map = {}

        if key is not None and value is not None:
            self._map[key] = value

    def append(self, key:str, value: object):
        if key not in self._map:
            self._map[key] = value
        return self
    
    def __str__(self):
        values = [self.convert(kv) for kv in self._map.items()]
        return "{" + ",".join(values) + "}"
    
    @staticmethod
    def convert(kv):
        value = str(kv[1])
        surround_with = '""' if '"' in value else '"'
        return kv[0] + ":" + surround_with + value + surround_with


if __name__ == '__main__':
    obj = ObjectValueStringBuilder()
    obj.append('name', 'tanaka taro')
    obj.append('age', 30)
    print(obj)