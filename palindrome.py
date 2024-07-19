# ЗАДАНИЕ
# - Напиши пошаговый алгоритм действий в комментариях для определения, является ли строка палиндромом.
#
# - Напишите по созданному вами алгоритму функцию для проверки, является ли строка палиндромом.
import string


def is_palindrome(s: str) -> bool:
    # Преобразование строки: приведение к нижнему регистру и удаление знаков препинания и пробелов
    s = s.lower()
    s = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "")

    # Определение длины строки
    length = len(s)

    # Сравнение символов
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False

    return True
