import src.model.word as word
import unittest

class TestWord(unittest.TestCase):

    def test_add_word(self):
        test_word = word.Word()
        test_word.add_word(0)

        assert(test_word._next == [[0, 1]])

        test_word.add_word(0)
        assert(test_word._next == [[0, 2]])

        test_word.add_word(1)
        assert(test_word._next == [[0, 2], [1, 1]])

    def test_is_end(self):
        pass

    def test_delete_cache(self):
        pass

    def test_next_word(self):
        pass
    