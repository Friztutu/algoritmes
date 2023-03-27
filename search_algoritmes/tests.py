from unittest import TestCase
from search_algoritmes.Searches import Searches
from search_algoritmes.exceptions import *


class SearchesTests(TestCase):

    def test_binary_search(self):
        self.assertEqual(Searches.binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3), 2)
        self.assertEqual(Searches.binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1), 0)
        self.assertEqual(Searches.binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8), 7)
        self.assertRaises(TypeError, Searches.binary_search, {1, 2, 3, 4, 5, 6, 7, 8}, 8)
        self.assertRaises(TypeError, Searches.binary_search, [1, '2', 3, 4, 5, 6, 7, 8], 8)
        self.assertRaises(SearchesUnsortedList, Searches.binary_search, [1, 2, 3, 5, 4, 6, 7, 8], 8)
        self.assertEqual(Searches.binary_search([], 0), -1)

    def test_linear_search(self):
        self.assertEqual(Searches.linear_search([1, 2, 3, 4, 5, 6, 7], 1), 0)
        self.assertEqual(Searches.linear_search([1, 2, 3, 4, 5, 6, 7], 9), -1)
        self.assertEqual(Searches.linear_search([1, 2, 3, 4, 5, 6, 7, '9'], '9'), 7)

