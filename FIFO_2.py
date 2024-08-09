class Node:

    __slots__ = ("value", "next")

    def __init__(self, value=None):
        self.value = value
        self.next = None


class FIFOQueue:
    '''
    В данной структуре я реализовал вспомогательный класс Node. Это позволило использовать памяти ровно столько сколько нам нужно.
    Так же реализовать это было значительно проще чем список и работать с этой структурой куда удобнее. Скорость работы должна быть схожа с прошлой реализацией.
    '''
    __slots__ = ("_capacity", "_size", "_front", "_back")

    def __init__(self, capacity, mass: list | tuple = None):
        self._capacity = capacity
        self._size = 0
        self._front = None
        self._back = None

        if mass:
            for i in mass[:capacity]:
                self.append(i)

    def append(self, value):
        new_node = Node(value)

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

    def get(self):
        if self._size == 0:
            return

        result = self._back.value
        self._back = self._back.next
        self._size -= 1
        return result

    def is_full(self):
        return self._size == self._capacity

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
def test_fifo_queue_initialization():
    # Инициализация пустой очереди
    queue = FIFOQueue(3)
    assert len(queue) == 0
    assert str(queue) == "[]"

    # Инициализация очереди с массивом меньшим, чем capacity
    queue = FIFOQueue(3, [1, 2])
    assert len(queue) == 2
    assert str(queue) == "[1, 2]"

    # Инициализация очереди с массивом равным capacity
    queue = FIFOQueue(3, [1, 2, 3])
    assert len(queue) == 3
    assert str(queue) == "[1, 2, 3]"

    # Инициализация очереди с массивом больше, чем capacity
    queue = FIFOQueue(3, [1, 2, 3, 4])
    assert len(queue) == 3
    assert str(queue) == "[1, 2, 3]"

def test_fifo_queue_append():
    # Добавление элементов в очередь
    queue = FIFOQueue(3)
    queue.append(1)
    assert len(queue) == 1
    assert str(queue) == "[1]"

    queue.append(2)
    assert len(queue) == 2
    assert str(queue) == "[1, 2]"

    queue.append(3)
    assert len(queue) == 3
    assert str(queue) == "[1, 2, 3]"

def test_fifo_queue_get():
    # Получение элементов из очереди
    queue = FIFOQueue(3, [1, 2, 3])
    assert queue.get() == 1
    assert len(queue) == 2
    assert str(queue) == "[2, 3]"

    assert queue.get() == 2
    assert len(queue) == 1
    assert str(queue) == "[3]"

    assert queue.get() == 3
    assert len(queue) == 0
    assert str(queue) == "[]"

    assert queue.get() is None  # Получение из пустой очереди

def test_fifo_queue_overflow():
    # Проверка переполнения очереди
    queue = FIFOQueue(3, [1, 2, 3])
    queue.append(4)  # Должен заменить первый элемент
    assert str(queue) == "[2, 3, 4]"
    assert queue.get() == 2
    assert str(queue) == "[3, 4]"

def test_fifo_queue_iteration():
    # Проверка итерации по очереди
    queue = FIFOQueue(3, [1, 2, 3])
    elements = [elem for elem in queue]
    assert elements == [1, 2, 3]

def test_fifo_queue_indexing():
    # Проверка доступа по индексу
    queue = FIFOQueue(3, [1, 2, 3])
    assert queue[0] == 1
    assert queue[1] == 2
    assert queue[2] == 3

    # Проверка изменения элементов по индексу
    queue[1] = 10
    assert queue[1] == 10
    assert str(queue) == "[1, 10, 3]"

def test_fifo_queue_boundary_conditions():
    # Проверка граничных условий
    queue = FIFOQueue(1)
    queue.append(1)
    assert queue.is_full()
    assert len(queue) == 1

    queue.append(2)  # Переполнение, должно заменить первый элемент
    assert queue.get() == 2
    assert len(queue) == 0

    queue.append(3)
    queue.append(4)  # Переполнение, должно заменить первый элемент
    assert queue.get() == 4

def test_fifo_queue_exceptions():
    queue = FIFOQueue(3, [1, 2, 3])

    try:
        _ = queue["a"]
    except TypeError as e:
        assert str(e) == "Ключ не является числом!"

    try:
        _ = queue[-1]
    except IndexError as e:
        assert str(e) == "Индекс вне диапазона!"

    try:
        queue[3] = 5
    except IndexError as e:
        assert str(e) == "Индекс вне диапазона!"

def run_all_tests():
    test_fifo_queue_initialization()
    test_fifo_queue_append()
    test_fifo_queue_get()
    test_fifo_queue_overflow()
    test_fifo_queue_iteration()
    test_fifo_queue_indexing()
    test_fifo_queue_boundary_conditions()
    test_fifo_queue_exceptions()
    print("Все тесты пройдены.")




if __name__ == "__main__":
    run_all_tests()