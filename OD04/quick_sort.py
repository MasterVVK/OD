import time
import random
import matplotlib.pyplot as plt
def quick_sort_iterative(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = arr[start]
        low, high = start, end

        while low < high:
            while low < high and arr[high] >= pivot:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] <= pivot:
                low += 1
            arr[high] = arr[low]

        arr[low] = pivot
        stack.append((start, low - 1))
        stack.append((low + 1, end))

    return arr


sizes = [10, 50, 100, 500, 1000]
times_best = []
times_avg = []
times_worst = []

# Лучший случай (случайный массив)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    quick_sort_iterative(arr)
    times_best.append(time.time() - start_time)

# Средний случай (частично отсортированный массив)
for size in sizes:
    arr = list(range(size))
    arr[size // 2:] = random.sample(range(size // 2, size), size // 2)
    start_time = time.time()
    quick_sort_iterative(arr)
    times_avg.append(time.time() - start_time)

# Худший случай (уже отсортированный массив)
for size in sizes:
    arr = list(range(size))
    start_time = time.time()
    quick_sort_iterative(arr)
    times_worst.append(time.time() - start_time)

# Построение графика
plt.figure(figsize=(12, 8))
plt.plot(sizes, times_best, label='Лучший случай (O(n log n))')
plt.plot(sizes, times_avg, label='Средний случай (O(n log n))')
plt.plot(sizes, times_worst, label='Худший случай (O(n^2))')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.title('Быстрая сортировка')
plt.grid(True)
plt.show()
