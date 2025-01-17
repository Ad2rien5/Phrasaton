import app.src.model.word as word
import unittest

class TestWord(unittest.TestCase):

    def setUp(self):
        self.test_word = word.Word('test')

    def test_add_word(self):
        self.test_word.add_word(0)

        self.assertEqual(self.test_word._next, [[0, 1]])

        self.test_word.add_word(0)
        self.assertEqual(self.test_word._next, [[0, 2]])

        self.test_word.add_word(1)
        self.assertEqual(self.test_word._next, [[0, 2], [1, 1]])

    def test_is_end(self):
        self.test_word.add_word(0)

        with self.assertRaises(AssertionError):
            self.test_word.is_end(0)

        self.test_word = word.Word('test')
        self.test_word.is_end(0)
        self.assertEqual(self.test_word._next, [[0, -1]])

    def test_next_word(self):
        with self.assertRaises(AssertionError):
            self.test_word.next_word()

        self.test_word.add_word(0)
        self.test_word.add_word(1)
        self.test_word.add_word(1)
        self.test_word.add_word(2)

        oracle = [1, 2, 0]
        test = [self.test_word.next_word() for _ in range(3)]
        self.assertEqual(test, oracle)

        self.assertEqual(self.test_word.next_word(), 0)


if __name__ == '__main__':
    unittest.main()