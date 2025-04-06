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

        self.dico.words.append(word.Word("test"))
        self.assertEqual(self.gv.get_index_leer()+1, self.dico.find("test"))


    def test_add_occurence(self):
        # assertion
        with self.assertRaises(AssertionError):
            self.dico.add_occurrence(453, "test")

        with self.assertRaises(AssertionError):
            self.dico.add_occurrence("test", 64)

        # two words unknowned
        self.dico.add_occurrence("a", "b")
        testa = self.dico.words[self.gv.get_index_leer()+1]
        testb = self.dico.words[self.gv.get_index_leer()+2]

        self.assertEqual("a", testa.value)
        self.assertEqual([[len(self.gv.PUNCTUATION)+2, 1]], testa._next)
        self.assertEqual("b", testb.value)

        # one unknowned word
        self.dico.add_occurrence("a", "c")
        testb = self.dico.words[len(self.gv.PUNCTUATION)+3]

        self.assertEqual(
            [[len(self.gv.PUNCTUATION)+2, 1], [len(self.gv.PUNCTUATION)+3, 1]],
            testa._next
        )
        self.assertEqual("c", testb.value) 

        self.dico.add_occurrence("d", "a")
        testb = self.dico.words[len(self.gv.PUNCTUATION)+4]

        self.assertEqual([[len(self.gv.PUNCTUATION)+2, 1], [len(self.gv.PUNCTUATION)+3, 1]], testa._next)
        self.assertEqual([[len(self.gv.PUNCTUATION)+1, 1]], testb._next)
        self.assertEqual("d", testb.value) 

        # two knowned
        self.dico.add_occurrence("d", "a")

        self.assertEqual([[len(self.gv.PUNCTUATION)+1, 2]], testb._next)
        self.assertEqual("d", testb.value) 

    def test_speak(self):
        pass

    def test_learn(self):
        # sentence badly ended
        for punc in range(len(self.gv.PUNCTUATION)):
            test = ("Ha", self.gv.PUNCTUATION[punc])

            try:
                self.dico.learn(test)
            except AssertionError as err:
                self.assertFalse(
                    punc in self.gv.SENTENCE_END, 
                    f"'{self.gv.PUNCTUATION[punc]}' is a valid ending punctuation, but throw '{err}'"
                )
        
        # word correctly added in the dictionnary
        index = self.dico.find("Ha")

        self.assertNotEqual(-1, index, "Failed to save word properly.")
        self.assertEqual(
            3, 
            len(self.dico.words[index]._next),
            "Failed to save word properly."
        )

    def test_learn2(self):
        return
        sentence = ("This", "sentence", "is", "a", "test", ".", "It", "ensure", "the", "correct", "working", "of", "the", "programm", ".")
        self.dico.learn(sentence)
        oracle = {
            "This": [[leer+2, 1]],
            "sentence": [[leer+3, 1]],
            "is": [[leer+4, 1]],
            "a": [[leer+5, 1]],
            "test": [[3, 1]],
            "It": [[leer+7, 1]],
            "ensure": [[leer+8, 1]],
        }
        leer = self.gv.get_index_leer()

        for punc in self.gv.PUNCTUATION:
            
            if punc == ".":
                oracle['.'] = [[leer, -1], [leer+1, 1], [leer+6, 1]]
            else:
                oracle[punc] = [[leer, -1], [leer+1, 1]]
        