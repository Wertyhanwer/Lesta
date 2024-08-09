"""
Алгоритм делит массив на две половины на каждом уровне рекурсии.
Это деление продолжается до тех пор, пока не останется подмассивы из одного элемента.
Количество уровней деления составляет log n, где n — количество элементов в массиве.
"""


def merge_sort(arr: list) -> list:

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left: int, right:int) -> list:
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(array)
    print("Отсортированный массив:", sorted_array)
