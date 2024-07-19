import pytest
from palindrome import is_palindrome

def test_palindrome_simple():
    assert is_palindrome("racecar") == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal, Panama") == True

def test_not_palindrome():
    assert is_palindrome("hello") == False

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True

def test_mixed_case_palindrome():
    assert is_palindrome("RaceCar") == True

def test_palindrome_with_numbers():
    assert is_palindrome("12321") == True

def test_not_palindrome_with_numbers():
    assert is_palindrome("12345") == False

# Новые тесты для проверки слов на русском языке
def test_russian_palindrome():
    assert is_palindrome("довод") == True

def test_russian_not_palindrome():
    assert is_palindrome("привет") == False

def test_russian_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("А роза упала на лапу Азора") == True

if __name__ == "__main__":
    pytest.main()
