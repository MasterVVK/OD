import time
import random
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list

sizes = [10, 50, 100, 500, 1000]
times_best = []
times_avg = []
times_worst = []

# Лучший случай (случайный массив)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    merge_sort(arr)
    times_best.append(time.time() - start_time)

# Средний случай (частично отсортированный массив)
for size in sizes:
    arr = list(range(size))
    arr[size//2:] = random.sample(range(size//2, size), size//2)
    start_time = time.time()
    merge_sort(arr)
    times_avg.append(time.time() - start_time)

# Худший случай (уже отсортированный массив)
for size in sizes:
    arr = list(range(size))
    start_time = time.time()
    merge_sort(arr)
    times_worst.append(time.time() - start_time)

# Построение графика
plt.figure(figsize=(12, 8))
plt.plot(sizes, times_best, label='Лучший случай (O(n log n))')
plt.plot(sizes, times_avg, label='Средний случай (O(n log n))')
plt.plot(sizes, times_worst, label='Худший случай (O(n log n))')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.title('Сортировка слиянием')
plt.grid(True)
plt.show()
