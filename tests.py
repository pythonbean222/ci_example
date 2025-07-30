"""Example."""
import unittest
import task


class TestCase(unittest.TestCase):
    """String.
    """

    def test1(self):
        """String.
        """
        expected = "Hello World"
        self.assertEqual(task.my_func(), expected)

    def test2(self):
        """String.
        """
        expected = "Hola World"
        self.assertEqual(task.my_func(), expected)


if __name__ == '__main__':
    unittest.main()
