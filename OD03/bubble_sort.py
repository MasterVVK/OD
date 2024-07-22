#Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    comparison_count = 0
    swap_count = 0
    for run in range(n-1):
        for i in range(n-1-run):
            comparison_count += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_count += 1
                print(f"Поменяли {arr[i]} и {arr[i + 1]}: {arr}")
    print(f"Количество сравнений: {comparison_count}")
    print(f"Количество обменов: {swap_count}")
    return arr

arr = [5, 7, 4, 3, 8, 2]
print("Исходный массив:", arr)
sorted_arr = bubble_sort(arr)
print("Отсортированный массив:", sorted_arr)

