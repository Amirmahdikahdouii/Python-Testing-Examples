import unittest
from traceback import format_exc
from first import first

class TestFirst(unittest.TestCase):
    def test_many(self):
        self.assertEqual(first((x for x in range(5))), 0)
        self.assertEqual(first((x for x in range(5)), "Default Value"), 0)

    def test_one(self):
        self.assertEqual(first([1]), 1)
        self.assertEqual(first([0], "Default Value"), 0)
    
    def test_default(self):
        self.assertEqual(first([], None), None)
        with self.assertRaises(TypeError):
            first(None, None)
    
    def test_stop_iteration(self):
        try:
            first([])
        except ValueError:
            formated_exc = format_exc()
            self.assertIn("StopIteration", formated_exc)
            self.assertIn("The above exception was the direct cause of the following exception", formated_exc)
            self.assertIn("ValueError: first() trying to return empty iterable first value", formated_exc)
        else:
            self.fail()
            
if __name__ == "__main__":
    unittest.main()