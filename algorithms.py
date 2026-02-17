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
class Algorithms:
    def __init__(self):
        pass

    # ---------------- BUBBLE SORT ----------------
    def bubble_sort(self, array):
        n = len(array)
        for i in range(n):
            for j in range(n - i - 1):
                # Compare
                yield ("compare", j, j + 1)
                if array[j] > array[j + 1]:
                    # Swap
                    array[j], array[j + 1] = array[j + 1], array[j]
                    yield ("swap", j, j + 1)
        yield ("sorted", -1, -1)

    # ---------------- SELECTION SORT ----------------
    def selection_sort(self, array):
        n = len(array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                yield ("compare", min_idx, j)
                if array[j] < array[min_idx]:
                    min_idx = j
            if min_idx != i:
                array[i], array[min_idx] = array[min_idx], array[i]
                yield ("swap", i, min_idx)
        yield ("sorted", -1, -1)

    # ---------------- INSERTION SORT ----------------
    def insertion_sort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                yield ("compare", j, i)
                array[j + 1] = array[j]
                yield ("overwrite", j + 1, j)
                j -= 1
            array[j + 1] = key
            yield ("overwrite", j + 1, i)
        yield ("sorted", -1, -1)

    # ---------------- MERGE SORT ----------------
    def merge_sort(self, array):
        yield from self._merge_sort(array, 0, len(array) - 1)

    def _merge_sort(self, array, left, right):
        if left < right:
            mid = (left + right) // 2
            yield from self._merge_sort(array, left, mid)
            yield from self._merge_sort(array, mid + 1, right)
            yield from self._merge(array, left, mid, right)

    def _merge(self, array, left, mid, right):
        left_copy = array[left:mid + 1]
        right_copy = array[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_copy) and j < len(right_copy):
            yield ("compare", left + i, mid + 1 + j)
            if left_copy[i] <= right_copy[j]:
                array[k] = left_copy[i]
                yield ("overwrite", k, left + i)
                i += 1
            else:
                array[k] = right_copy[j]
                yield ("overwrite", k, mid + 1 + j)
                j += 1
            k += 1

        while i < len(left_copy):
            array[k] = left_copy[i]
            yield ("overwrite", k, left + i)
            i += 1
            k += 1

        while j < len(right_copy):
            array[k] = right_copy[j]
            yield ("overwrite", k, mid + 1 + j)
            j += 1
            k += 1

    # ---------------- QUICK SORT ----------------
    def quick_sort(self, array):
        yield from self._quick_sort(array, 0, len(array) - 1)

    def _quick_sort(self, array, low, high):
        if low < high:
            pivot_index, gen = self._partition(array, low, high)
            yield from gen
            yield from self._quick_sort(array, low, pivot_index - 1)
            yield from self._quick_sort(array, pivot_index + 1, high)

    def _partition(self, array, low, high):
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
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                yield ("swap", i, j)
        array[i + 1], array[high] = array[high], array[i + 1]
        yield ("swap", i + 1, high)
        return i + 1, iter([])
