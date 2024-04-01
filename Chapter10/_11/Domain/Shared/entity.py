from unit_of_work import UnitOfWork

class Entity:
    def __init__(self) -> None:
        self.unit_of_work = UnitOfWork()

    def mark_new(self):
        self.unit_of_work.register_new(self)

    def mark_clean(self):
        self.unit_of_work.register_clean(self)

    def mark_dirty(self):
        self.unit_of_work.register_dirty(self)

    def mark_deleted(self):
        self.unit_of_work.register_deleted(self)


if __name__ == '__main__':
    entity = Entity()
    entity.mark_clean()
