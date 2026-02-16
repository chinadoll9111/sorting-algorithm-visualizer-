# algorithms.py

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            yield ("compare", j, j+1)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                yield ("swap", j, j+1)
    yield ("sorted", None, None)


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            yield ("compare", min_idx, j)
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            yield ("swap", i, min_idx)
    yield ("sorted", None, None)


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and array[j] > key:
            yield ("compare", j, i)
            array[j+1] = array[j]
            yield ("overwrite", j+1, array[j])
            j -= 1
        array[j+1] = key
        yield ("overwrite", j+1, key)
    yield ("sorted", None, None)


def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(array, start, mid)
        yield from merge_sort(array, mid, end)
        left = array[start:mid]
        right = array[mid:end]
        i = j = 0
        for k in range(start, end):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                array[k] = left[i]
                yield ("overwrite", k, left[i])
                i += 1
            else:
                array[k] = right[j]
                yield ("overwrite", k, right[j])
                j += 1
    if start == 0:
        yield ("sorted", None, None)


def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    def partition(low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            yield ("compare", j, high)
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                yield ("swap", i, j)
        array[i+1], array[high] = array[high], array[i+1]
        yield ("swap", i+1, high)
        return i+1

    if start < end:
        pi_gen = partition(start, end)
        pi = None
        while True:
            try:
                op = next(pi_gen)
                yield op
            except StopIteration as e:
                pi = e.value
                break
        left = quick_sort(array, start, pi-1)
        yield from left
        right = quick_sort(array, pi+1, end)
        yield from right
    if start == 0 and end == len(array) - 1:
        yield ("sorted", None, None)
