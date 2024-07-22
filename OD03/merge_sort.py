#Сортировка слиянием

comparison_count = 0


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    global comparison_count
    sorted_list = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        comparison_count += 1
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    print(f"Слияние: {sorted_list}")
    return sorted_list


arr = [38, 27, 43, 3, 9, 82, 10]
print("Исходный массив:", arr)
sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)
print(f"Количество сравнений: {comparison_count}")
