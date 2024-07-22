#Сортировка выбором


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Минимальный элемент на позиции {i}: {arr}")
    return arr

arr = [-3, 5, 0, -8, 1, 10]
print("Исходный массив:", arr)
sorted_arr = selection_sort(arr)
print("Отсортированный массив:", sorted_arr)
