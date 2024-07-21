#Стек (LIFO - Last In, First Out)
# __init__: Конструктор, инициализирующий пустой список.
# is_empty: Проверяет, пуст ли стек.
# push: Добавляет элемент в конец списка.
# pop: Удаляет и возвращает последний элемент списка. Если стек пуст, выбрасывается исключение IndexError.
# peek: Возвращает последний элемент списка без его удаления. Если стек пуст, выбрасывается исключение IndexError.
# size: Возвращает количество элементов в стеке.
# __str__: Возвращает строковое представление стека.


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(3)
stack.push(4)
print(stack)          # Output: [1, 2, 3]
print(stack.pop())    # Output: 3
print(stack)
print(stack.peek())   # Output: 2
print(stack.size())   # Output: 2
print(stack.is_empty())  # Output: False
print(stack)
