class UnitOfWork:
    def register_new(self, value: object) -> None:
        raise NotImplementedError()
    
    def register_dirty(self, value: object) -> None:
        raise NotImplementedError()
    
    def register_clean(self, value: object) -> None:
        raise NotImplementedError()
    
    def register_deleted(self, value: object) -> None:
        raise NotImplementedError()
    
    def commit(self, value: object) -> None:
        raise NotImplementedError()


if __name__ == '__main__':
    unit_of_work = UnitOfWork()
    unit_of_work.register_new('111-222-333')