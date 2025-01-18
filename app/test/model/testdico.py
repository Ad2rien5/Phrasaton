import app.src.model.dico as dico
import app.src.model.word as word
import app.src.model.global_value as global_value
import unittest

class TestDico(unittest.TestCase):

    def setUp(self):
        self.dico = dico.Dico()
        self.gv = global_value.GlobalValue()

    def test_init(self):
        oracle = []
        oracle.extend(self.gv.PUNCTUATION)
        oracle.append('leer')
        test = [
            self.dico.words[i].value for i in range(len(self.dico.words))
        ]

        self.assertEqual(oracle, test)

        for nb in self.gv.SENTENCE_END:
            self.assertEqual(self.dico.words[nb]._next, [[6, -1]])


    def test_find(self):
        # wronf type
        with self.assertRaises(AssertionError):
            self.dico.find(1)

        # not find
        self.assertEqual(-1, self.dico.find("test"))

        # find
        oracle = [i for i in range(len(self.gv.PUNCTUATION))]
        oracle.append(self.gv.get_index_leer())

        test = [self.dico.find(j.value) for j in self.dico.words]

        self.assertEqual(oracle, test)

        self.dico.words(word.Word("test"))
        self.assertEqual(self.gv.get_index_leer()+1, self.dico.find("test"))



    def test_add_occurence(self):
        pass

    def test_reset_cache(self):
        pass

    def test_speak(self):
        pass

    def test_learn(self):
        pass
