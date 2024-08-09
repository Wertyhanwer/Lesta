from BaseFIFO import BaseFIFO


class FIFOQueue(BaseFIFO):
    """
    В данной структуре я реализовал вспомогательный класс Node. Это позволило использовать памяти ровно столько сколько нам нужно.
    Так же реализовать это было значительно проще чем список и работать с этой структурой куда удобнее. Скорость работы должна быть схожа с прошлой реализацией.
    """
    __slots__ = ("_capacity", "_size", "_front", "_back")

    class _Node:
        __slots__ = ("value", "next")

        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self._front = None
        self._back = None

    def append(self, value):
        new_node = self._Node(value)

        if self._size == 0:
            self._front = self._back = new_node
            self._size += 1

        else:

            if self._size == self._capacity:
                self._front.next = self._back
                self._front = self._back
                self._back = self._back.next
                self._front.value = new_node.value

            else:
                self._front.next = new_node
                self._front = new_node
                self._size += 1

    def pop(self):
        if self._size == 0:
            return

        result = self._back.value
        self._back = self._back.next
        self._size -= 1
        return result

    def is_full(self):
        return self._size == self._capacity

    def clear(self):
        while self._size != 0:
            self.pop()

    def __str__(self):
        if self._size == 0:
            return "[]"

        result = []
        current = self._back
        for _ in range(self._size):
            result.append(current.value)
            current = current.next

        return str(result)

    def __repr__(self):
        return f"FIFOQueue({self._capacity}, {self.__str__()})"

    def __len__(self):
        return self._size

    def __eq__(self, other):
        if isinstance(other, FIFOQueue):
            return self.__str__() == other.__str__()

        else:
            return NotImplemented

    def __iter__(self):
        current = self._back
        for _ in range(self._size):
            result = current.value
            current = current.next
            yield result

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Ключ не является числом!")

        if key < 0 or key >= self._size:
            raise IndexError("Индекс вне диапазона!")

        current = self._back
        for _ in range(key):
            current = current.next

        return current.value

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Ключ не является числом!")

        if key < 0 or key >= self._size:
            raise IndexError("Индекс вне диапазона!")

        current = self._back
        for _ in range(key):
            current = current.next

        current.value = value

