from unittest import TestCase
from search_algoritmes.Searches import Searches
from search_algoritmes.exceptions import *


class SearchesTests(TestCase):

    def binary_search_tests(self):
        self.assertEqual(Searches.binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3), 2)
        self.assertEqual(Searches.binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1), 2)
        self.assertEqual(Searches.binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8), 2)
        self.assertRaises(SearchesIncorrectType, Searches.binary_search(), {1, 2, 3, 4, 5, 6, 7, 8}, 8)
        self.assertRaises(SearchesIncorrectType, Searches.binary_search(), [1, '2', 3, 4, 5, 6, 7, 8], 8)
        self.assertRaises(SearchesUnsortedList, Searches.binary_search(), [1, 2, 3, 5, 4, 6, 7, 8], 8)

