from BaseFIFO import BaseFIFO


class FifoList(BaseFIFO):
    """
    Это реализация на базе Динамического массива. Хоть и сделан на базе списка но доступ к элементу через [] от O(1) до O(N).
    Так как буфер циклический то нет разницы в скорости удаления или добавления элементов, но из за этого
    поедается лишняя память даже когда ячейки в массиве пустуют.
    """

    __slots__ = ("_size", "_buffer", "_begin", "_end", "_full")

    def __init__(self, size: int):
        self._size = size
        self._buffer = [None] * size
        self._begin = 0
        self._end = 0
        self._full = False

    @property
    def full(self):
        return self._full

    @property
    def size(self):
        return self._size

    def append(self, item):
        if self._full:
            self._begin = (self._begin + 1) % self._size

        self._buffer[self._end] = item
        self._end = (self._end + 1) % self._size

        if self._end == self._begin:
            self._full = True

    def pop(self):
        if self.__len__() == 0:
            return

        result = self._buffer[self._begin]
        self._buffer[self._begin] = None
        self._begin = (self._begin + 1) % self._size
        self._full = False
        return result

    def clear(self):
        self._buffer = [None] * self._size
        self._begin = 0
        self._end = 0

    def __repr__(self):
        return f"FifoList({self._size}, {self._buffer})"

    def __str__(self):
        result = []
        index = self._begin

        for _ in range(0, self.__len__()):
            result.append(self._buffer[index])
            index = (index + 1) % self._size

        return str(result)

    def __len__(self):
        if self._end > self._begin:
            return self._end - self._begin

        if self._end < self._begin:
            return self._size-self._begin + self._end + 1

        if self._full:
            return self._size

        return 0

    def __eq__(self, other):
        if isinstance(other, FifoList):
            return self.__str__() == other.__str__()

        else:
            return False

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Значение ключа должно быть числом!")

        if key < 0 or key >= self.__len__():
            raise IndexError("Индекс вне диапазона!")

        return self._buffer[(self._begin + key) % self._size]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Значение ключа должно быть числом!")

        if key < 0 or key >= self.__len__():
            raise IndexError("Индекс вне диапазона!")

        self._buffer[(self._begin + key) % self._size] = value

    def __iter__(self):
        index = self._begin
        count = 0
        while count < self.__len__():
            yield self._buffer[index]
            index = (index + 1) % self._size
            count += 1



