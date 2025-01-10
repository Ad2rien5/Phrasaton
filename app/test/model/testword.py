import src.model.word as word
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

    def test_delete_cache(self):
        pass

    def test_next_word(self):
        pass

if __name__ == '__main__':
    unittest.main()