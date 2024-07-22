#Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for run in range(n-1):
        for i in range(n-1-run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print(f"Поменяли {arr[i]} и {arr[i + 1]}: {arr}")
    return arr

arr = [5, 7, 4, 3, 8, 2]
print("Исходный массив:", arr)
sorted_arr = bubble_sort(arr)
print("Отсортированный массив:", sorted_arr)
