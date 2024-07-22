#Быстрая сортировка с классами

class QuickSort:
    def __init__(self):
        self.comparison_count = 0

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        self.comparison_count += len(arr) - 1
        print(f"Опорный элемент: {pivot}; Лево: {left}; Право: {right}")
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

arr = [7, 6, 10, 5, 9, 8, 3, 4]
sorter = QuickSort()
print("Исходный массив:", arr)
sorted_arr = sorter.quick_sort(arr)
print("Отсортированный массив:", sorted_arr)
print(f"Количество сравнений: {sorter.comparison_count}")
