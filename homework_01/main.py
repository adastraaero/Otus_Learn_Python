"""
Домашнее задание №1
Функции и структуры данных
"""
from sympy import *

def power_numbers(*numbers, power=2):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = []
    for number in numbers:
        result.append(number ** power)
    print(result)

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def ODD(n):
    return n % 2 != 0

def EVEN(n):
    return n % 2 == 0

def PRIME(n):
    return isprime(n)

def filter_numbers(check, spisok):
    print(list(filter(spisok, check)))


    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
