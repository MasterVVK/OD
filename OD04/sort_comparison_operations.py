import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for run in range(n-1):
        for i in range(n-1-run):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
    return arr, comparisons, swaps

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return arr, comparisons, swaps

def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
        comparisons += 1  # Для последнего сравнения в while
    return arr, comparisons, swaps

def quick_sort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return arr, comparisons
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    comparisons += len(arr) - 1
    left_sorted, left_comparisons = quick_sort(left)
    right_sorted, right_comparisons = quick_sort(right)
    return left_sorted + [pivot] + right_sorted, comparisons + left_comparisons + right_comparisons

def merge_sort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return arr, comparisons
    mid = len(arr) // 2
    left, left_comparisons = merge_sort(arr[:mid])
    right, right_comparisons = merge_sort(arr[mid:])
    sorted_arr, merge_comparisons = merge(left, right)
    return sorted_arr, comparisons + left_comparisons + right_comparisons + merge_comparisons

def merge(left, right):
    sorted_list = []
    comparisons = 0
    while left and right:
        comparisons += 1
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list, comparisons

sizes = [10, 50, 100, 500, 1000]
comparisons_bubble = []
comparisons_selection = []
comparisons_insertion = []
comparisons_quick = []
comparisons_merge = []

# Пузырьковая сортировка (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons, _ = bubble_sort(arr)
    comparisons_bubble.append(comparisons)

# Сортировка выбором (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons, _ = selection_sort(arr)
    comparisons_selection.append(comparisons)

# Сортировка вставками (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons, _ = insertion_sort(arr)
    comparisons_insertion.append(comparisons)

# Быстрая сортировка (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons = quick_sort(arr)
    comparisons_quick.append(comparisons)

# Сортировка слиянием (Средний случай)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons = merge_sort(arr)
    comparisons_merge.append(comparisons)

# Построение графика сравнений
plt.figure(figsize=(12, 8))
plt.plot(sizes, comparisons_bubble, label='Пузырьковая сортировка (O(n^2))')
plt.plot(sizes, comparisons_selection, label='Сортировка выбором (O(n^2))')
plt.plot(sizes, comparisons_insertion, label='Сортировка вставками (O(n^2))')
plt.plot(sizes, comparisons_quick, label='Быстрая сортировка (O(n log n))')
plt.plot(sizes, comparisons_merge, label='Сортировка слиянием (O(n log n))')
plt.xlabel('Размер массива')
plt.ylabel('Количество сравнений')
plt.legend()
plt.title('Сравнение временных сложностей алгоритмов сортировки (сравнения)')
plt.grid(True)
plt.show()
