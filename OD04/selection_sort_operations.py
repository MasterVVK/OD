import time
import random
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
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

sizes = [10, 50, 100, 500, 1000]
comparisons_best = []
swaps_best = []
comparisons_avg = []
swaps_avg = []
comparisons_worst = []
swaps_worst = []

# Лучший случай (уже отсортированный массив)
for size in sizes:
    arr = list(range(size))
    _, comparisons, swaps = selection_sort(arr)
    comparisons_best.append(comparisons)
    swaps_best.append(swaps)

# Средний случай (случайный массив)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons, swaps = selection_sort(arr)
    comparisons_avg.append(comparisons)
    swaps_avg.append(swaps)

# Худший случай (обратный порядок)
for size in sizes:
    arr = list(range(size, 0, -1))
    _, comparisons, swaps = selection_sort(arr)
    comparisons_worst.append(comparisons)
    swaps_worst.append(swaps)

# Построение графика сравнений
plt.figure(figsize=(12, 8))
plt.plot(sizes, comparisons_best, label='Лучший случай (O(n^2))')
plt.plot(sizes, comparisons_avg, label='Средний случай (O(n^2))')
plt.plot(sizes, comparisons_worst, label='Худший случай (O(n^2))')
plt.xlabel('Размер массива')
plt.ylabel('Количество сравнений')
plt.legend()
plt.title('Сортировка выбором - сравнения')
plt.grid(True)
plt.show()

# Построение графика обменов
plt.figure(figsize=(12, 8))
plt.plot(sizes, swaps_best, label='Лучший случай (O(n^2))')
plt.plot(sizes, swaps_avg, label='Средний случай (O(n^2))')
plt.plot(sizes, swaps_worst, label='Худший случай (O(n^2))')
plt.xlabel('Размер массива')
plt.ylabel('Количество обменов')
plt.legend()
plt.title('Сортировка выбором - обмены')
plt.grid(True)
plt.show()
