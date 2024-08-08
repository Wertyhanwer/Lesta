


class FifoList:
    '''
    Это реализация на базе Динамического массива. Хоть и сделан на базе списка но доступ к элементу через [] от O(1) до O(N).
    Так как буфер циклический то нет разницы в скорости удаления или добавления элементов, но из за этого
    поедается лишняя память даже когда ячейки в массиве пустуют.
    '''

    __slots__ = ("_size", "_buffer", "_begin", "_end", "_full")

    def __init__(self, size: int, collection: list | tuple = None):
        self._size = size
        self._buffer = [None] * size
        self._begin = 0
        self._end = 0
        self._full = False

        if collection:
            for item in collection[:size]:
                self._buffer[self._end] = item
                self._end = (self._end + 1) % self._size

            if self._end == self._begin:
                self._full = True

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

    def get(self):
        if self.__len__() == 0:
            return
        result = self._buffer[self._begin]
        self._buffer[self._begin] = None
        self._begin = (self._begin + 1) % self._size
        self._full = False
        return result

    def clear(self):
        self._buffer = [None]*self._size
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
        elif self._end < self._begin:
            return self._size-self._begin + self._end + 1
        elif self._full:
            return self._size
        else:
            return 0

    def __eq__(self, other):
        if isinstance(other, FifoList):
            return self.__str__() == other.__str__()
        else:
            return NotImplemented

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


def test_fifo_list():
    # Тест инициализации с коллекцией и без
    fifo1 = FifoList(5)
    assert len(fifo1) == 0, "Ошибка: Пустой FifoList должен иметь длину 0"

    fifo2 = FifoList(5, [1, 2, 3])
    assert len(fifo2) == 3, "Ошибка: Длина FifoList после инициализации с коллекцией неверна"
    assert fifo2[0] == 1 and fifo2[1] == 2 and fifo2[2] == 3, "Ошибка: Неверные значения в FifoList после инициализации с коллекцией"

    # Тест добавления элементов
    fifo1.append(10)
    assert len(fifo1) == 1, "Ошибка: Длина FifoList после добавления элемента неверна"
    assert fifo1[0] == 10, "Ошибка: Неверное значение в FifoList после добавления элемента"

    fifo1.append(20)
    assert len(fifo1) == 2, "Ошибка: Длина FifoList после добавления второго элемента неверна"
    assert fifo1[1] == 20, "Ошибка: Неверное значение в FifoList после добавления второго элемента"

    # Тест удаления элементов
    item = fifo1.get()
    assert item == 10, "Ошибка: Неверное значение удалено из FifoList"
    assert len(fifo1) == 1, "Ошибка: Длина FifoList после удаления элемента неверна"

    # Тест цикличности буфера
    for i in range(4):
        fifo1.append(i)

    assert fifo1.full, "Ошибка: FifoList должен быть полон"
    fifo1.append(5)
    assert fifo1.get() == 0, "Ошибка: Неверное значение удалено из FifoList после переполнения"

    # Тест __getitem__ и __setitem__
    fifo1[0] = 100
    assert fifo1[0] == 100
    fifo2[0] = 100
    assert fifo2[0] == 100, "Ошибка: Неверное значение после установки нового значения через __setitem__"

    # Тест __repr__ и __str__
    assert repr(fifo2) == "FifoList(5, [100, 2, 3, None, None])", "Ошибка: Неверный вывод __repr__"
    assert str(fifo2) == "[100, 2, 3]", "Ошибка: Неверный вывод __str__"

    # Тест clear
    fifo2.clear()
    assert len(fifo2) == 0, "Ошибка: Длина FifoList после очистки должна быть 0"

    # Тест __eq__
    fifo3 = FifoList(5, [1, 2, 3])
    fifo4 = FifoList(5, [1, 2, 3])
    assert fifo3 == fifo4, "Ошибка: Два одинаковых FifoList должны быть равны"

    print("Все тесты пройдены успешно!")


if __name__ == '__main__':
    test_fifo_list()
    pablo = FifoList(5)
