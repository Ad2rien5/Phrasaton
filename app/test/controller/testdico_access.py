import random
import string
import unittest

import app.src.controller.dico_access as dico_access
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

            self.assertEqual(self.dico_access._punctuation(word, char), oracle)

    def test_punctuation2(self) -> None:
        for char in self.gv.PUNCTUATION:
            word : str = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )

            with self.assertRaises(AssertionError):
                self.dico_access._punctuation(word, char)

    def test_punctuation3(self) -> None:
        for char in self.gv.PUNCTUATION:
            randstr: str = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            word: str = randstr + char + randstr

            result, punc = self.dico_access._punctuation(word, char)
            self.assertEqual(result, randstr)
            self.assertEqual(punc, char+randstr)

    def test_detection_classic(self) -> None:
        test : tuple = self.dico_access._detection("test", 0)
        oracle : tuple = (0, "test", None)

        self.assertEqual(test, oracle)

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
            self.assertEqual(test, oracle, f"|start|\nstart : {nb_start}; substract : {nb_parenthesis}")

            # at the end
            nb_start = random.randint(5, 15)
            nb_parenthesis = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            ) + sign * nb_parenthesis
            test = self.dico_access._detection(mot, nb_start)
            oracle = (nb_start - nb_parenthesis, mot, None)
            self.assertEqual(test, oracle, f"|end|\nstart : {nb_start}; substract : {nb_parenthesis}")

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
            self.assertEqual(test, oracle, f"|middle|\nstart : {nb_start}; substract : {nb_parenthesis}")

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
                mot,
                None
            )
            self.assertEqual(
                test, oracle,
                f"|everywhere|\nstart : {nb_start}; begin : {nb_parenthesis}; middle : {nb_parenthesis_mid}; end : {nb_parenthesis_end}"
            )

    def test_detection_parenthesis_both(self) -> None:
        for num_sign in range(len(self.gv.PARENTHESIS_END)):
            open_sign = self.gv.PARENTHESIS_START[num_sign]
            close_sign = self.gv.PARENTHESIS_END[num_sign]

            # at the start
            nb_start : int = random.randint(15, 35)
            nb_parenthesis_o : int = random.randint(1, 5)
            nb_parenthesis_c : int = random.randint(1, 5)
            mot : str = (
                open_sign * nb_parenthesis_o + 
                close_sign * nb_parenthesis_c +
                "".join(
                    random.choice(string.ascii_letters)
                    for _ in range(random.randint(5, 15))
                )
            )
            test : tuple = self.dico_access._detection(mot, nb_start)
            oracle : tuple = (
                nb_start - nb_parenthesis_c + nb_parenthesis_o, 
                mot, 
                None
            )
            self.assertEqual(test, oracle, f"|start|\nstart : {nb_start}; open : {nb_parenthesis_o}; close : {nb_parenthesis_c};")

            # at the end
            nb_start : int = random.randint(15, 35)
            nb_parenthesis_o : int = random.randint(1, 5)
            nb_parenthesis_c : int = random.randint(1, 5)
            mot = (
                "".join(
                    random.choice(string.ascii_letters)
                    for _ in range(random.randint(5, 15))
                ) + 
                open_sign * nb_parenthesis_o + 
                close_sign * nb_parenthesis_c
            )
            test = self.dico_access._detection(mot, nb_start)
            oracle : tuple = (
                nb_start - nb_parenthesis_c + nb_parenthesis_o, 
                mot, 
                None
            )
            self.assertEqual(test, oracle, f"|end|\nstart : {nb_start}; open : {nb_parenthesis_o}; close : {nb_parenthesis_c};")

            # in the middle
            nb_start : int = random.randint(15, 35)
            nb_parenthesis_o : int = random.randint(1, 5)
            nb_parenthesis_c : int = random.randint(1, 5)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            mot += open_sign*nb_parenthesis_o + close_sign*nb_parenthesis_c + mot
            test = self.dico_access._detection(mot, nb_start)
            oracle : tuple = (
                nb_start - nb_parenthesis_c + nb_parenthesis_o, 
                mot, 
                None
            )
            self.assertEqual(test, oracle, f"|middle|\nstart : {nb_start}; open : {nb_parenthesis_o}; close : {nb_parenthesis_c};")

            # everywhere
            nb_start : int = random.randint(15, 35)
            nb_parenthesis_o : int = random.randint(1, 5)
            nb_parenthesis_c : int = random.randint(1, 5)
            nb_parenthesis_mid : int = random.randint(1, 3)
            nb_parenthesis_end : int = random.randint(1, 3)
            mot = "".join(
                random.choice(string.ascii_letters)
                for _ in range(random.randint(5, 15))
            )
            mot = (
                    open_sign*nb_parenthesis_o +
                    close_sign*nb_parenthesis_c +
                    mot + 
                    open_sign*nb_parenthesis_mid*nb_parenthesis_o +
                    close_sign*nb_parenthesis_mid*nb_parenthesis_c +
                    mot + 
                    open_sign*nb_parenthesis_end*nb_parenthesis_o + 
                    close_sign*nb_parenthesis_end*nb_parenthesis_c
            )
            test = self.dico_access._detection(
                mot, nb_start
            )
            total_o : int = nb_parenthesis_o*(1+nb_parenthesis_mid+nb_parenthesis_end)
            total_c : int = nb_parenthesis_c*(1+nb_parenthesis_mid+nb_parenthesis_end)
            oracle = (
                nb_start + total_o - total_c,
                mot, 
                None
            )
            self.assertEqual(
                test, oracle,
                f"|everywhere|\nstart : {nb_start}; open : {nb_parenthesis_o}; close : {nb_parenthesis_c}; middle : {nb_parenthesis_mid}; end : {nb_parenthesis_end}"
            )

    def test_detection_punctuation(self) -> None:
        for punc in self.gv.PUNCTUATION:
            nb_paren, word, punctuation = self.dico_access._detection(f"word{punc}", 0)
            self.assertEqual(nb_paren, 0)
            self.assertEqual(word, "word")
            self.assertEqual(punctuation, punc)

    def test_detection_punctuation_parenthesis(self) -> None:
        for punc in self.gv.PUNCTUATION:
            for sign in range(len(self.gv.PARENTHESIS_START)):
                # before
                nb_paren, word, punctuation = self.dico_access._detection(f"{self.gv.PARENTHESIS_START[sign]}word{punc}", 0)
                self.assertEqual(nb_paren, 1)
                self.assertEqual(word, f"{self.gv.PARENTHESIS_START[sign]}word")
                self.assertEqual(punctuation, punc)

                # after
                nb_paren, word, punctuation = self.dico_access._detection(f"word{punc}{self.gv.PARENTHESIS_END[sign]}", 0)
                self.assertEqual(nb_paren, -1)
                self.assertEqual(word, "word")
                self.assertEqual(punctuation, f"{punc}{self.gv.PARENTHESIS_END[sign]}")
                self.assertEqual(punctuation, punc+self.gv.PARENTHESIS_END[sign])

                # both
                nb_paren, word, punctuation = self.dico_access._detection(f"{self.gv.PARENTHESIS_START[sign]}word{punc}{self.gv.PARENTHESIS_END[sign]}", 0)
                self.assertEqual(nb_paren, 0)
                self.assertEqual(word, f"{self.gv.PARENTHESIS_START[sign]}word")
                self.assertEqual(punctuation, f"{punc}{self.gv.PARENTHESIS_END[sign]}")
                self.assertEqual(punctuation, punc+self.gv.PARENTHESIS_END[sign])