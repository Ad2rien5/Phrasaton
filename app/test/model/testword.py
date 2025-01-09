import app.src.model.word as word
import unittest

class TestWord(unittest.TestCase):

    def test_add_word(self):
        test_word = word.Word('test')
        test_word.add_word(0)

        self.assertEqual(test_word._next, [[0, 1]])

        test_word.add_word(0)
        self.assertEqual(test_word._next, [[0, 2]])

        test_word.add_word(1)
        self.assertEqual(test_word._next, [[0, 2], [1, 1]])

    def test_is_end(self):
        test_word = word.Word('t')
        test_word.add_word(0)

        with self.assertRaises(AssertionError):
            test_word.is_end(0)

        test_word = word.Word('test')
        test_word.is_end(0)
        self.assertEqual(test_word._next, [[0, -1]])

    def test_delete_cache(self):
        pass

    def test_next_word(self):
        pass

if __name__ == '__main__':
    unittest.main()