from abc import ABC, abstractmethod


class BaseFIFO(ABC):

    @abstractmethod
    def append(self, value): ...

    @abstractmethod
    def pop(self): ...

    @abstractmethod
    def clear(self): ...
