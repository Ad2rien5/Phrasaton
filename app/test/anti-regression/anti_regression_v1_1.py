import unittest

import app.src.controller.dico_access as dico_access
from app.src.model.dico import Dico
from app.src.model.global_value import GlobalValue


class ARv11(unittest.TestCase):

    def setUp(self):
        self.dico_access : dico_access.DicoAccess = dico_access.DicoAccess()
        self.gv : GlobalValue = GlobalValue()



    def test_learn(self) -> None:
        # setup
        sentence : str = "Hello, your name is Phrasaton. This sentence is a test sentence."
        self.dico_access.save_dico_data(sentence)
        words : list[str] = sentence.split()
        # split comma and point
        words[0] = words[0][:-1]
        words[4] = words[4][:-1]
        words[10] = words[10][:-1]
        words.append(".")
        words.insert(5, ".")
        words.insert(1, ",")

        # verification
        dico : Dico = self.dico_access.dico

        for  currentIt in range(len(words)):
            actualw : int = dico.find(words[currentIt]) if currentIt in [1, 6, 13] else dico.find(" " + words[currentIt])

            if currentIt == len(words) - 1:
                nextw : int = dico.find("leer")
            elif currentIt + 1 not in [1, 6, 13]:
                # word gain a space before them (for indentation, where symbol don't)
                nextw: int = dico.find(" " + words[currentIt + 1])
            else :
                nextw : int = dico.find(words[currentIt + 1])

            self.assertTrue(dico.words[actualw].know_word(nextw),
                            f"{words[currentIt]} should have known the next one.")


    def test_talk(self) -> None:
        # demande une phrase
        # vérifie si la suite de mot est retrouvée
        pass