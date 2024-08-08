from random import randint
import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения {func.__name__} - {end - start} секунд")
        return result

    return inner


def quick_sort(lst: list) -> list:
    '''
    Хорошо работает со всеми видами массивов
    '''
    if len(lst) <= 1:
        return lst
    x = lst[len(lst) // 2]
    left = [i for i in lst if i < x]
    middle = [i for i in lst if i == x]
    right = [i for i in lst if i > x]
    return main(left) + middle + main(right)

def insertion_sort(lst):
    '''
    Работает лучше всего с небольшими массивами
    '''
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def main(lst: list) -> list:
    if len(lst) > 100:
        return quick_sort(lst)
    else:
        return insertion_sort(lst)


if __name__ == '__main__':
    list_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    list_2 = [randint(1,100000) for _ in range(1000)]
    list_3 = list(range(1000000,0,-1))

    start = time.perf_counter()
    print(main(list_1))
    end = time.perf_counter()
    print(f"Время выполнения: {end - start} секунд")

    start = time.perf_counter()
    print(main(list_2))
    end = time.perf_counter()
    print(f"Время выполнения: {end - start} секунд")

    start = time.perf_counter()
    print(main(list_3))
    end = time.perf_counter()
    print(f"Время выполнения: {end - start} секунд")
