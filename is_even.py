import time


# Функции выводят True если число чётное и False если число нечётное


def timer(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения {func.__name__} - {end - start} секунд")
        return result

    return inner


@timer
def primer(n):
    '''
    Функция из примера
    '''
    return n % 2 == 0


@timer
def main(n):
    '''
    Эта функция работает быстрее чем % 2 хотя разница практически минимальна.
    '''
    return not bool(n & 1)


@timer
def IQ_400(n):
    '''
    Это Rofls... Но тоже как рабочий способ и даже иногда быстрее ( для больших чисел ) чем функция из примера.
    '''
    return not bool(int(bin(n)[-1]))


if __name__ == '__main__':
    n = 37423472470237
    print(primer(n))
    print(main(n))
    print(IQ_400(n))
