import app.src.model.dico as dico
import app.src.model.word as word
import app.src.model.global_value as global_value
import unittest


class TestDico(unittest.TestCase):

    def setUp(self) -> None:
        self.dico : dico.Dico = dico.Dico()
        self.gv : global_value.GlobalValue = global_value.GlobalValue()

    def test_init(self):
        oracle : list[str] = []
        oracle.extend(self.gv.PUNCTUATION)
        oracle.append('leer')
        test : list[str] = [
            self.dico.words[i].value for i in range(len(self.dico.words))
        ]

        self.assertEqual(test, oracle)

        for nb in self.gv.SENTENCE_END:
            self.assertEqual(self.dico.words[nb]._next, [[6, -1]])

    def test_find(self) -> None:
        # not find
        self.assertEqual(self.dico.find("test"), -1)

        # find
        oracle : list[int] = [i for i in range(len(self.gv.PUNCTUATION))]
        oracle.append(self.gv.get_index_leer())

        test : list[int] = [self.dico.find(j.value) for j in self.dico.words]

        self.assertEqual(test, oracle)

        self.dico.words.append(word.Word("test"))
        self.assertEqual(self.dico.find("test"), self.gv.get_index_leer() + 1)

    def test_add_occurrence(self) -> None:
        # two words unknown
        self.dico.add_occurrence("a", "b")
        testa : word.Word = self.dico.words[self.gv.get_index_leer() + 1]
        testb : word.Word = self.dico.words[self.gv.get_index_leer() + 2]

        self.assertEqual(testa.value, "a")
        self.assertEqual(testa._next, [[len(self.gv.PUNCTUATION) + 2, 1]])
        self.assertEqual(testb.value, "b")

        # one unknown word
        self.dico.add_occurrence("a", "c")
        testb = self.dico.words[len(self.gv.PUNCTUATION) + 3]

        self.assertEqual(
            testa._next,
            [[len(self.gv.PUNCTUATION) + 2, 1], [len(self.gv.PUNCTUATION) + 3, 1]]
        )
        self.assertEqual(testb.value, "c")

        self.dico.add_occurrence("d", "a")
        testb = self.dico.words[len(self.gv.PUNCTUATION) + 4]

        self.assertEqual(testa._next, [[len(self.gv.PUNCTUATION) + 2, 1], [len(self.gv.PUNCTUATION) + 3, 1]])
        self.assertEqual(testb._next, [[len(self.gv.PUNCTUATION) + 1, 1]])
        self.assertEqual(testb.value, "d")

        # two known
        self.dico.add_occurrence("d", "a")

        self.assertEqual(testb._next, [[len(self.gv.PUNCTUATION) + 1, 2]])
        self.assertEqual(testb.value, "d")

    def test_learn(self) -> None:
        # sentence badly ended
        for punc in range(len(self.gv.PUNCTUATION)):
            test : tuple[str, str] = ("Ha", self.gv.PUNCTUATION[punc])

            try:
                self.dico.learn(test)
            except AssertionError as err:
                self.assertFalse(
                    punc in self.gv.SENTENCE_END,
                    f"'{self.gv.PUNCTUATION[punc]}' is a valid ending punctuation, but throw '{err}'"
                )

        # word correctly added in the dictionary
        index : int = self.dico.find("Ha")

        self.assertNotEqual(index, -1, "Failed to save word properly.")
        self.assertEqual(
            len(self.dico.words[index]._next),
            3,
            "Failed to save word properly."
        )

    def test_learn2(self) -> None:
        # set-up
        leer : int = self.gv.get_index_leer()
        sentence : tuple[str, ...]= ("This", "sentence", "is", "a", "test", ".", "It", "ensure", "the", "correct", "working", "of",
                    "the", "program", ".")
        oracle = {
            "leer": [],
            "This": [[leer + 2, 1]],
            "sentence": [[leer + 3, 1]],
            "is": [[leer + 4, 1]],
            "a": [[leer + 5, 1]],
            "test": [[3, 1]],
            "It": [[leer + 7, 1]],
            "ensure": [[leer + 8, 1]],
            "the": [[leer + 9, 1], [leer + 12, 1]],
            "correct": [[leer + 10, 1]],
            "working": [[leer + 11, 1]],
            "of": [[leer + 8, 1]],
            "program": [[3, 1]]
        }

        stc_end = self.gv.end_sent_str()

        for punc in self.gv.PUNCTUATION:

            if punc == ".":
                oracle['.'] = [[leer, -1], [leer + 1, 1], [leer + 6, 1]]
            elif punc in stc_end:
                oracle[punc] = [[leer, -1], [leer + 1, 1]]
            else:
                oracle[punc] = []

        # test
        self.dico.learn(sentence)

        for element in self.dico.words:
            self.assertEqual(element._next, oracle[element.value], f"'{element.value}' failed")

    def test_speak(self):
        # test the assertion
        with self.assertRaises(AssertionError):
            self.dico.speak()

        self.dico.nbSentences = 1
        with self.assertRaises(AssertionError):
            self.dico.speak()

        # test a real case
        self.dico.learn(
            (" This", " sentence", " is", " a", " test", ".", " It", " ensure", " the", " correct", " working", " of",
             " the", " program", "."))
        oracle = " This sentence is a test."

        self.dico.nbSentences = 1
        test = self.dico.speak()
        self.assertEqual(test, oracle)

        self.dico.nbSentences = 2
        oracle = " This sentence is a test. It ensure the correct working of the program."
        test = self.dico.speak()
        self.assertEqual(test, oracle)
