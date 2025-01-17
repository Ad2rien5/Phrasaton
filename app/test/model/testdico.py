import app.src.model.dico as dico
import app.src.model.word as word
import app.src.model.global_value as global_value
import unittest

class TestDico(unittest.TestCase):

    def setUp(self):
        self.test_dico = dico.Dico()
        self.gv = global_value.GlobalValue()
        self.test_word = word.Word('test')

    def test_init(self):
        oracle = [
            "?", ",", ";", ".", ":", "!", "leer"
        ]
        test = [
            self.test_dico.words[i].value for i in range(len(self.test_dico.words))
        ]

        self.assertEqual(oracle, test)

        for nb in self.gv.SENTENCE_END:
            self.assertEqual(self.test_dico.words[nb]._next, [[6, -1]])


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
