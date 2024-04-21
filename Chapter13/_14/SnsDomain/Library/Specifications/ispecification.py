from abc import ABC, abstractmethod

class ISpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, value):
        pass
