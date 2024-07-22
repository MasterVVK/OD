#Сортировка вставками

def insert_sort(arr):
    comparison_count = 0
    swap_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparison_count += 1
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1
        arr[j + 1] = key
        print(f"Вставка элемента на позицию {i}: {arr}")
    print(f"Количество сравнений: {comparison_count}")
    print(f"Количество обменов: {swap_count}")
    return arr

arr = [-3, 5, 0, -8, 1, 10]
print("Исходный массив:", arr)
sorted_arr = insert_sort(arr)
print("Отсортированный массив:", sorted_arr)
