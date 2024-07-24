import time
import random
import matplotlib.pyplot as plt

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
comparisons_best = []
comparisons_avg = []
comparisons_worst = []

# Лучший случай (случайный массив)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons = merge_sort(arr)
    comparisons_best.append(comparisons)

# Средний случай (частично отсортированный массив)
for size in sizes:
    arr = list(range(size))
    arr[size//2:] = random.sample(range(size//2, size), size//2)
    _, comparisons = merge_sort(arr)
    comparisons_avg.append(comparisons)

# Худший случай (уже отсортированный массив)
for size in sizes:
    arr = list(range(size))
    _, comparisons = merge_sort(arr)
    comparisons_worst.append(comparisons)

# Построение графика сравнений
plt.figure(figsize=(12, 8))
plt.plot(sizes, comparisons_best, label='Лучший случай (O(n log n))')
plt.plot(sizes, comparisons_avg, label='Средний случай (O(n log n))')
plt.plot(sizes, comparisons_worst, label='Худший случай (O(n log n))')
plt.xlabel('Размер массива')
plt.ylabel('Количество сравнений')
plt.legend()
plt.title('Сортировка слиянием - сравнения')
plt.grid(True)
plt.show()
