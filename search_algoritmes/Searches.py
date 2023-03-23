from typing import Iterable
from search_algoritmes.exceptions import *


class Searches:

    @classmethod
    def binary_search(cls, array: Iterable, target: int) -> int:
        cls.__validator_binary_search(array, target)

        left, right = 0, len(array) - 1

        while left <= right:
            middle = (right + left) // 2
            num = array[middle]
            if num > target:
                right = middle - 1
            elif num < target:
                left = middle + 1
            else:
                return middle

        return -1

    @staticmethod
    def __validator_binary_search(array: Iterable, target: int):
        if not array:
            raise ValueError('Был передан пустой список')

        if not isinstance(array, (list, tuple)):
            raise TypeError('Выполнить поиск элемента можно только в кортеже или списке')

        if type(target) not in (int, float):
            raise TypeError('Target может быть только числом')

        if not all(map(lambda x: type(x) in (int, float), array)):
            raise TypeError('Содержание массива не может быть не числом')

        if not sorted(array) == array:
            raise SearchesUnsortedList('Нельзя передавать неотсортированные коллекции')
