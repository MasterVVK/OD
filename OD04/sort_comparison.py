import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for run in range(n-1):
        for i in range(n-1-run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

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
times_bubble = []
times_selection = []
times_insertion = []
times_quick = []
times_merge = []

# Пузырьковая сортировка (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    bubble_sort(arr)
    times_bubble.append(time.time() - start_time)

# Сортировка выбором (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    selection_sort(arr)
    times_selection.append(time.time() - start_time)

# Сортировка вставками (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    insertion_sort(arr)
    times_insertion.append(time.time() - start_time)

# Быстрая сортировка (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    quick_sort(arr)
    times_quick.append(time.time() - start_time)

# Сортировка слиянием (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    merge_sort(arr)
    times_merge.append(time.time() - start_time)

# Построение графика
plt.figure(figsize=(12, 8))
plt.plot(sizes, times_bubble, label='Пузырьковая сортировка (O(n^2))')
plt.plot(sizes, times_selection, label='Сортировка выбором (O(n^2))')
plt.plot(sizes, times_insertion, label='Сортировка вставками (O(n^2))')
plt.plot(sizes, times_quick, label='Быстрая сортировка (O(n log n))')
plt.plot(sizes, times_merge, label='Сортировка слиянием (O(n log n))')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.title('Сравнение временных сложностей алгоритмов сортировки')
plt.grid(True)
plt.show()
