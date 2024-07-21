#Очередь (FIFO - First In, First Out)

# __init__: Конструктор, инициализирующий пустой список.
# is_empty: Проверяет, пуста ли очередь.
# enqueue: Добавляет элемент в конец списка.
# dequeue: Удаляет и возвращает первый элемент списка. Если очередь пуста, выбрасывается исключение IndexError.
# size: Возвращает количество элементов в очереди.
# __str__: Возвращает строковое представление очереди.


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Пример использования очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(4)
print(queue)          # Output: [1, 2, 3]
print(queue.dequeue())  # Output: 1
print(queue.size())     # Output: 2
print(queue.is_empty())  # Output: False
print(queue)
