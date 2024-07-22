#Сортировка выборомdef selection_sort(arr):
def selection_sort(arr):
    n = len(arr)
    comparison_count = 0
    swap_count = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparison_count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swap_count += 1
        print(f"Минимальный элемент на позиции {i}: {arr}")
    print(f"Количество сравнений: {comparison_count}")
    print(f"Количество обменов: {swap_count}")
    return arr


arr = [-3, 5, 0, -8, 1, 10]
print("Исходный массив:", arr)
sorted_arr = selection_sort(arr)
print("Отсортированный массив:", sorted_arr)
