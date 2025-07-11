import random
import string

import app.src.controller.dico_access as dico_access
import unittest

from app.src.model import global_value


class TestDicoAccess(unittest.TestCase):

    def setUp(self) -> None:
        self.dico_access : dico_access.DicoAccess = dico_access.DicoAccess()
        self.gv : global_value.GlobalValue = global_value.GlobalValue()

    def test_purge_bad_char1(self) -> None:
        """
        Case
        ____
        Word without any bad character
        """
        test : str = self.dico_access._purge_bad_char("test")
        self.assertEqual(test, "test", f"test != {test}")

        # test with a special character
        test = self.dico_access._purge_bad_char("champêtre")
        self.assertEqual(test, "champêtre", f"champêtre != {test}")

    def test_purge_bad_char2(self) -> None:
        """
        Case
        ----
        Word containing a bad character
        """
        for char in self.gv.BAD_CHAR:
            word : str = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            i : int = random.randint(1, len(word))
            word = word[:i] + char + word[i:]
            oracle : str = word.replace(char, "")
            test : str = self.dico_access._purge_bad_char(word)

            self.assertEqual(
                test,
                oracle,
                f"{oracle} != {test}"
            )

    def test_purge_bad_char3(self) -> None:
        """
        Case
        ----
        Only one bad character
        """
        for char in self.gv.BAD_CHAR:
            with self.assertRaises(AssertionError):
                self.dico_access._purge_bad_char(char)

    def test_punctuation1(self) -> None:
        for char in self.gv.PUNCTUATION:
            word : str = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            ) + char

            oracle : tuple[str, str] = (word[:-1], char)

            self.assertEqual(self.dico_access._punctuation(word), oracle)

    def test_punctuation2(self) -> None:
        for _ in range(100):
            word : str = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )

            with self.assertRaises(AssertionError):
                self.dico_access._punctuation(word)

    def test_detection1(self) -> None:
        test : tuple = self.dico_access._detection("test", 0)
        oracle : tuple = (0, "test", None)

        self.assertEqual(test, oracle)

        #TODO
        # - parenthèse ouvrante
        # - parenthèse fermante

    def test_detection_parenthesis_open(self) -> None:
        for sign in self.gv.PARENTHESIS_START:
            # at the start
            nb_start : int = random.randint(1, 10)
            nb_parenthesis : int = random.randint(1, 5)
            mot : str = sign*nb_parenthesis + "".join(
                    random.choice(string.ascii_letters)
                    for _ in range(random.randint(5, 15))
            )
            test : tuple = self.dico_access._detection(mot, nb_start)
            oracle : tuple = (nb_start+nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|start|\nstart : {nb_start}; add : {nb_parenthesis}")

            # at the end
            nb_start = random.randint(1, 10)
            nb_parenthesis = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            ) + sign*nb_parenthesis
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
            mot += sign*nb_parenthesis + mot
            test = self.dico_access._detection(mot, nb_start)
            oracle = (nb_start + nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|middle|\nstart : {nb_start}; add : {nb_parenthesis}")

            # everywhere
            nb_start = random.randint(1, 10)
            nb_parenthesis = random.randint(1, 5)
            nb_parenthesis_mid : int = random.randint(1, 5)
            nb_parenthesis_end : int = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            mot = (
                sign*nb_parenthesis +
                mot + sign*nb_parenthesis_mid +
                mot + sign*nb_parenthesis_end
           )
            test = self.dico_access._detection(
                mot, nb_start
            )
            oracle = (
                nb_start + nb_parenthesis + nb_parenthesis_mid + nb_parenthesis_end,
                mot, None
            )
            self.assertEqual(
                test, oracle,
                f"|everywhere|\nstart : {nb_start}; begin : {nb_parenthesis}; middle : {nb_parenthesis_mid}; end : {nb_parenthesis_end}"
            )

    def test_detection_parenthesis_close(self) -> None:
        for sign in self.gv.PARENTHESIS_END:
            # at the start
            nb_start : int = random.randint(5, 15)
            nb_parenthesis : int = random.randint(1, 5)
            mot : str = sign * nb_parenthesis + "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            test : tuple = self.dico_access._detection(mot, nb_start)
            oracle : tuple = (nb_start - nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|start|\nstart : {nb_start}; add : {nb_parenthesis}")

            # at the end
            nb_start = random.randint(5, 15)
            nb_parenthesis = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            ) + sign * nb_parenthesis
            test = self.dico_access._detection(mot, nb_start)
            oracle = (nb_start - nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|end|\nstart : {nb_start}; add : {nb_parenthesis}")

            # in the middle
            nb_start = random.randint(5, 15)
            nb_parenthesis = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            mot += sign * nb_parenthesis + mot
            test = self.dico_access._detection(mot, nb_start)
            oracle = (nb_start - nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|middle|\nstart : {nb_start}; add : {nb_parenthesis}")

            # everywhere
            nb_start = random.randint(5, 15)
            nb_parenthesis = random.randint(1, 5)
            nb_parenthesis_mid : int = random.randint(1, 5)
            nb_parenthesis_end : int = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            mot = (
                    sign * nb_parenthesis +
                    mot + sign * nb_parenthesis_mid +
                    mot + sign * nb_parenthesis_end
            )
            test = self.dico_access._detection(
                mot, nb_start
            )
            oracle = (
                nb_start - nb_parenthesis - nb_parenthesis_mid - nb_parenthesis_end,
                mot, None
            )
            self.assertEqual(
                test, oracle,
                f"|everywhere|\nstart : {nb_start}; begin : {nb_parenthesis}; middle : {nb_parenthesis_mid}; end : {nb_parenthesis_end}"
            )