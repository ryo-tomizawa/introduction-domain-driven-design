from abc import ABC, abstractmethod

class IUnitOfWork:
    @property
    @abstractmethod
    def user_property(self):
        pass

    @abstractmethod
    def commit(self):
        pass


if __name__ == '__main__':
    iunit_of_work = IUnitOfWork()

    # 具体的な処理は記載していないためNone
    print(iunit_of_work.user_property)
    print(iunit_of_work.commit())