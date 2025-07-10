import random
import string

import app.src.controller.dico_access as dico_access
import unittest

from app.src.model import global_value


class TestDicoAccess(unittest.TestCase):

    def setUp(self):
        self.dico_access = dico_access.DicoAccess()
        self.gv = global_value.GlobalValue()

    def test_purge_bad_char1(self):
        """
        Case
        ____
        Word without any bad character
        """
        test = self.dico_access._purge_bad_char("test")
        self.assertEqual("test", test, f"test != {test}")

        # test with a special character
        test = self.dico_access._purge_bad_char("champêtre")
        self.assertEqual("champêtre", test, f"champêtre != {test}")

    def test_purge_bad_char2(self):
        """
        Case
        ----
        Word containing a bad character
        """
        for char in self.gv.BAD_CHAR:
            word = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            i = random.randint(1, len(word))
            word = word[:i] + char + word[i:]
            oracle = word.replace(char, "")
            test = self.dico_access._purge_bad_char(word)

            self.assertEqual(
                oracle,
                test,
                f"{oracle} != {test}"
            )

    def test_purge_bad_char3(self):
        """
        Case
        ----
        Only one bad character
        """
        for char in self.gv.BAD_CHAR:
            with self.assertRaises(AssertionError):
                self.dico_access._purge_bad_char(char)

    def test_punctuation1(self):
        for char in self.gv.PUNCTUATION:
            word = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            ) + char

            oracle = (word[:-1], char)

            self.assertEqual(oracle, self.dico_access._punctuation(word))

    def test_punctuation2(self):
        for _ in range(100):
            word = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )

            with self.assertRaises(AssertionError):
                self.dico_access._punctuation(word)

    def test_detection1(self):
        test = self.dico_access._detection("test", 0)
        oracle = (0, "test", None)

        self.assertEqual(test, oracle)

        #TODO
        # - parenthèse ouvrante
        # - parenthèse fermante

    def test_detection_parenthesis_open(self):
        for _ in range(100):
            # at the start
            nb_start = random.randint(1, 10)
            nb_parenthesis = random.randint(1, 5)
            mot = "("*nb_parenthesis + "".join(
                    random.choice(string.ascii_letters)
                    for _ in range(random.randint(5, 15))
            )
            test = self.dico_access._detection(mot, nb_start)
            oracle = (nb_start+nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|start|\nstart : {nb_start}; add : {nb_parenthesis}")

            # at the end
            nb_start = random.randint(1, 10)
            nb_parenthesis = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            ) + "("*nb_parenthesis
            test = self.dico_access._detection(mot, nb_start)
            oracle = (nb_start + nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|end|\nstart : {nb_start}; add : {nb_parenthesis}")

            # in the middle
            nb_start = random.randint(1, 10)
            nb_parenthesis = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            mot += "("*nb_parenthesis + mot
            test = self.dico_access._detection(mot, nb_start)
            oracle = (nb_start + nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|middle|\nstart : {nb_start}; add : {nb_parenthesis}")

            # everywhere
            nb_start = random.randint(1, 10)
            nb_parenthesis = random.randint(1, 5)
            nb_parenthesis_mid = random.randint(1, 5)
            nb_parenthesis_end = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            mot = (
                "("*nb_parenthesis +
                mot + "("*nb_parenthesis_mid +
                mot + "("*nb_parenthesis_end
           )
            test = self.dico_access._detection(
                mot, nb_start
            )
            oracle = (
                nb_start + nb_parenthesis + nb_parenthesis_mid + nb_parenthesis_end,
                mot, None
            )
            self.assertEqual(test, oracle, f"|everywhere|\nstart : {nb_start}; begin : {nb_parenthesis}; middle : {nb_parenthesis_mid}; end : {nb_parenthesis_end}")

