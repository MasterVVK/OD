#Быстрая сортировка
comparison_count = 0

def quick_sort(arr):
    global comparison_count
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    comparison_count += len(arr) - 1
    print(f"Опорный элемент: {pivot}; Лево: {left}; Право: {right}")
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [7, 6, 10, 5, 9, 8, 3, 4]
print("Исходный массив:", arr)
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)
print(f"Количество сравнений: {comparison_count}")

