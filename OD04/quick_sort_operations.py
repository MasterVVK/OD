import time
import random
import matplotlib.pyplot as plt
import sys

# Увеличиваем максимальную глубину рекурсии
sys.setrecursionlimit(2000)

def median_of_three(arr):
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    return sorted([first, middle, last])[1]

def quick_sort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return arr, comparisons
    pivot = median_of_three(arr)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    comparisons += len(arr) - 1
    left_sorted, left_comparisons = quick_sort(left)
    right_sorted, right_comparisons = quick_sort(right)
    return left_sorted + middle + right_sorted, comparisons + left_comparisons + right_comparisons

sizes = [10, 50, 100, 500, 1000]
comparisons_best = []
comparisons_avg = []
comparisons_worst = []

# Лучший случай (случайный массив)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons = quick_sort(arr)
    comparisons_best.append(comparisons)

# Средний случай (частично отсортированный массив)
for size in sizes:
    arr = list(range(size))
    arr[size//2:] = random.sample(range(size//2, size), size//2)
    _, comparisons = quick_sort(arr)
    comparisons_avg.append(comparisons)

# Худший случай (уже отсортированный массив)
for size in sizes:
    arr = list(range(size))
    _, comparisons = quick_sort(arr)
    comparisons_worst.append(comparisons)

# Построение графика сравнений
plt.figure(figsize=(12, 8))
plt.plot(sizes, comparisons_best, label='Лучший случай (O(n log n))')
plt.plot(sizes, comparisons_avg, label='Средний случай (O(n log n))')
plt.plot(sizes, comparisons_worst, label='Худший случай (O(n^2))')
plt.xlabel('Размер массива')
plt.ylabel('Количество сравнений')
plt.legend()
plt.title('Быстрая сортировка - сравнения')
plt.grid(True)
plt.show()
