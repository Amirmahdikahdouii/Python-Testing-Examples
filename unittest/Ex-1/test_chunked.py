import unittest
from chunked import slice_iterable, chunked


class TestSliceIterable(unittest.TestCase):
    default_test_iterable = []

    @classmethod
    def setUpClass(cls):
        cls.default_test_iterable = list(range(1, 6))
        return super().setUpClass()

    def test_null_iterable(self):
        self.assertEqual(slice_iterable([], 10), [])
        self.assertEqual(slice_iterable([], 0), [])
        self.assertRaises(TypeError, lambda: slice_iterable(number=10))

    def test_null_number(self):
        self.assertEqual(slice_iterable(self.default_test_iterable, 0), [])
        self.assertRaises(TypeError, lambda: slice_iterable(
            self.default_test_iterable))

    def test_value(self):
        self.assertEqual(slice_iterable(
            self.default_test_iterable, 3), [1, 2, 3])
        self.assertEqual(slice_iterable(range(10), 5), [0, 1, 2, 3, 4])

    def test_number(self):
        self.assertEqual(slice_iterable(
            self.default_test_iterable, 12), self.default_test_iterable)
        self.assertRaises(ValueError, lambda: slice_iterable(
            self.default_test_iterable, 2.5))
        self.assertRaises(ValueError, lambda: slice_iterable(
            self.default_test_iterable, -2))


class TestChunked(unittest.TestCase):
    default_even_value = []
    default_odd_value = []

    @classmethod
    def setUpClass(cls):
        cls.default_even_value = list(range(1, 7))
        cls.default_odd_value = list(range(1, 6))
        return super().setUpClass()

    def test_value(self):
        self.assertEqual(
            list(chunked(self.default_odd_value, 3)), [[1, 2, 3], [4, 5]]
        )
        self.assertEqual(
            list(chunked(self.default_odd_value, 2)), [[1, 2], [3, 4], [5]]
        )
        self.assertEqual(
            list(chunked(self.default_even_value, 3)), [[1, 2, 3], [4, 5, 6]]
        )
        self.assertEqual(
            list(chunked(self.default_even_value, 2)), [[1, 2], [3, 4], [5, 6]]
        )
        self.assertEqual(
            list(chunked(self.default_even_value, 4)), [[1, 2, 3, 4], [5, 6]]
        )

    def test_strick(self):
        self.assertRaises(ValueError, lambda: list(
            chunked(self.default_even_value, 4, strick=True)))
        
        self.assertEqual(
            list(chunked(self.default_even_value, 3, True)), [
                [1, 2, 3], [4, 5, 6]]
        )
        self.assertRaises(ValueError, lambda: list(
            chunked(self.default_odd_value, 2, True)))

    def test_none(self):
        self.assertRaises(ValueError, lambda: chunked(
            self.default_even_value, None))

    def test_numbers(self):
        self.assertRaises(ValueError, lambda: chunked(
            self.default_even_value, 2.5))
        
        self.assertRaises(ValueError, lambda: chunked(
            self.default_even_value, -5))
        
        self.assertEqual(list(chunked(self.default_even_value, 110)), [
                         [1, 2, 3, 4, 5, 6]])
        
        self.assertEqual(list(chunked(self.default_odd_value, 1)), [
                         [1], [2], [3], [4], [5]])


if __name__ == "__main__":
    unittest.main()
