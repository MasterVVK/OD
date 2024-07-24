import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sizes = [10, 50, 100, 500, 1000]
times_best = []
times_avg = []
times_worst = []

# Лучший случай (уже отсортированный массив)
for size in sizes:
    arr = list(range(size))
    start_time = time.time()
    insertion_sort(arr)
    times_best.append(time.time() - start_time)

# Средний случай (случайный массив)
for size in sizes:
    arr = random.sample(range(size * 2), size)
    start_time = time.time()
    insertion_sort(arr)
    times_avg.append(time.time() - start_time)

# Худший случай (обратный порядок)
for size in sizes:
    arr = list(range(size, 0, -1))
    start_time = time.time()
    insertion_sort(arr)
    times_worst.append(time.time() - start_time)

# Построение графика
plt.figure(figsize=(12, 8))
plt.plot(sizes, times_best, label='Лучший случай (O(n))')
plt.plot(sizes, times_avg, label='Средний случай (O(n^2))')
plt.plot(sizes, times_worst, label='Худший случай (O(n^2))')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.legend()
plt.title('Сортировка вставками')
plt.grid(True)
plt.show()
