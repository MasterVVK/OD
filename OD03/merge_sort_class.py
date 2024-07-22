#Сортировка слиянием с классами 
class MergeSort:
    def __init__(self):
        self.comparison_count = 0

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        sorted_list = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            self.comparison_count += 1
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
sorter = MergeSort()
print("Исходный массив:", arr)
sorted_arr = sorter.merge_sort(arr)
print("Отсортированный массив:", sorted_arr)
print(f"Количество сравнений: {sorter.comparison_count}")
