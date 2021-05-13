import unittest

from sorted_frozen_set import SortedFrozenSet

class TestConstruction(unittest.TestCase):

    def test_construct_empty(self):
        s = SortedFrozenSet([])

    def test_construct_nonempty_list(self):
        s = SortedFrozenSet([2, 4, 9])

    def test_construct_from_iterator(self):
        items = [2, 4, 9]
        iterator = iter(items)
        s = SortedFrozenSet(iterator)

    def test_construct_no_args(self):
        s = SortedFrozenSet()

class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedFrozenSet([3, 4, 6, 9])

    def test_positive_contained(self):
        self.assertTrue(3 in self.s)

    def test_negative_contained(self):
        self.assertFalse(5 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(7 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)

class TestIterableProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedFrozenSet([7, 5, 5, 3, 8])

    def test_iter(self):
        iterator = iter(self.s)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 5)
        self.assertEqual(next(iterator), 7)
        self.assertEqual(next(iterator), 8)
        self.assertEqual(
            StopIteration,
            lambda: next(iterator)
        )



if __name__ == '__main__':
    unittest.main()