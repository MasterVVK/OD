#Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    print(f"Опорный элемент: {pivot}; Лево: {left}; Право: {right}")
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [7, 6, 10, 5, 9, 8, 3, 4]
print("Исходный массив:", arr)
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)
