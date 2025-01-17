import app.src.model.dico as dico
import app.src.model.word as word
import unittest

class TestDico(unittest.TestCase):

    def setUp(self):
        self.test_dico = dico.Dico()

        self.test_word = word.Word('test')

    def test_find(self):
        pass

    def test_add_occurence(self):
        pass

    def test_reset_cache(self):
        pass

    def test_speak(self):
        pass

    def test_learn(self):
        pass
