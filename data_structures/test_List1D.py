import unittest
from List1D import List1D


class List1DTest(unittest.TestCase):

    def test_push_back(self):
        test_list = List1D()
        test_list.push_back(6)
        self.assertEqual(test_list.head, 6)
        self.assertEqual(len(test_list), 1)
        test_list.push_back(5)
        self.assertEqual(test_list[-1], 5)
        self.assertEqual(len(test_list), 2)
        test_list.push_back(4)
        self.assertEqual(test_list[-1], 4)
        self.assertEqual(len(test_list), 3)
        self.assertEqual(test_list.head, 6)

    def test_push_front(self):
        test_list = List1D()
        test_list.push_front(1)
        self.assertEqual(test_list.head, 1)
        self.assertEqual(len(test_list), 1)
        test_list.push_front(2)
        self.assertEqual(test_list.head, 2)
        self.assertEqual(len(test_list), 2)
        self.assertEqual(test_list[-1], 1)
        test_list.push_front(3)
        self.assertEqual(test_list.head, 3)
        self.assertEqual(len(test_list), 3)
        self.assertEqual(test_list[-1], 1)

    def test_pop_back(self):
        test_list = List1D((1, 2, 3))
        self.assertEqual(test_list.pop_back(), 3)
        self.assertEqual(len(test_list), 2)
        self.assertEqual(test_list[-1], 2)
        self.assertEqual(test_list.pop_back(), 2)
        self.assertEqual(len(test_list), 1)
        self.assertEqual(test_list[-1], 1)
        self.assertEqual(test_list.pop_back(), 1)
        self.assertEqual(len(test_list), 0)
        self.assertRaises(IndexError, test_list.__getitem__, -1)
        self.assertRaises(ValueError, test_list.pop_back)

    def test_pop_front(self):
        test_list = List1D([1, 2, 3])
        self.assertEqual(test_list.pop_front(), 1)
        self.assertEqual(len(test_list), 2)
        self.assertEqual(test_list.head, 2)
        self.assertEqual(test_list.pop_front(), 2)
        self.assertEqual(len(test_list), 1)
        self.assertEqual(test_list.head, 3)
        self.assertEqual(test_list.pop_front(), 3)
        self.assertEqual(len(test_list), 0)
        self.assertEqual(test_list.head, None)
        self.assertRaises(ValueError, test_list.pop_front)

    def test_insert(self):
        test_list = List1D()
        test_list.insert(10, 5)
        self.assertEqual(test_list.head, 5)
        test_list.insert(0, 6)
        self.assertEqual(test_list.head, 6)
        test_list.insert(1, 7)
        self.assertEqual(test_list[1], 7)
        test_list.insert(-1, 8)
        self.assertEqual(test_list[3], 8)


if __name__ == '__main__':
    unittest.main()
