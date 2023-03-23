from unittest import TestCase
from Searches import Searches


class SearchesTests(TestCase):

    def binary_search_tests(self):
        self.assertEqual(Searches.binary_search([1, 2, 3, 4, 5, 6, 7, 8]), 2)

