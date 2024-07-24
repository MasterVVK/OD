import time
import random
import matplotlib.pyplot as plt

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
    _, comparisons, swaps = insertion_sort(arr)
    comparisons_best.append(comparisons)
    swaps_best.append(swaps)

# Средний случай (случайный массив)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    _, comparisons, swaps = insertion_sort(arr)
    comparisons_avg.append(comparisons)
    swaps_avg.append(swaps)

# Худший случай (обратный порядок)
for size in sizes:
    arr = list(range(size, 0, -1))
    _, comparisons, swaps = insertion_sort(arr)
    comparisons_worst.append(comparisons)
    swaps_worst.append(swaps)

# Построение графика сравнений
plt.figure(figsize=(12, 8))
plt.plot(sizes, comparisons_best, label='Лучший случай (O(n))')
plt.plot(sizes, comparisons_avg, label='Средний случай (O(n^2))')
plt.plot(sizes, comparisons_worst, label='Худший случай (O(n^2))')
plt.xlabel('Размер массива')
plt.ylabel('Количество сравнений')
plt.legend()
plt.title('Сортировка вставками - сравнения')
plt.grid(True)
plt.show()

# Построение графика обменов
plt.figure(figsize=(12, 8))
plt.plot(sizes, swaps_best, label='Лучший случай (O(n))')
plt.plot(sizes, swaps_avg, label='Средний случай (O(n^2))')
plt.plot(sizes, swaps_worst, label='Худший случай (O(n^2))')
plt.xlabel('Размер массива')
plt.ylabel('Количество обменов')
plt.legend()
plt.title('Сортировка вставками - обмены')
plt.grid(True)
plt.show()
