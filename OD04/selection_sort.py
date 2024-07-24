import time
import random
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

sizes = [10, 50, 100, 500, 1000]
times_best = []
times_avg = []
times_worst = []

# Лучший случай (уже отсортированный массив)
for size in sizes:
    arr = list(range(size))
    start_time = time.time()
    selection_sort(arr)
    times_best.append(time.time() - start_time)

# Средний случай (случайный массив)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    selection_sort(arr)
    times_avg.append(time.time() - start_time)

# Худший случай (обратный порядок)
for size in sizes:
    arr = list(range(size, 0, -1))
    start_time = time.time()
    selection_sort(arr)
    times_worst.append(time.time() - start_time)

# Построение графика
plt.figure(figsize=(12, 8))
plt.plot(sizes, times_best, label='Лучший случай (O(n^2))')
plt.plot(sizes, times_avg, label='Средний случай (O(n^2))')
plt.plot(sizes, times_worst, label='Худший случай (O(n^2))')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.title('Сортировка выбором')
plt.grid(True)
plt.show()
