import app.src.controller.dico_access as dico_access
import unittest

class TestDicoAccess(unittest.TestCase):

    def test_purge_bad_char(self):
        #TODO
        # - mot sans problème (change pas)
        # - un cas par char problématique
        # - un char qui est problématique (assert catch)
        pass

    def test_punctuation(self):
        #TODO
        # - un cas par signe de ponctuation
        # - sans signe de ponctuation (assert)
        pass

    def test_detection(self):
        #TODO
        # - implémentation de purge_bad_char
        # - parenthèse ouvrante
        # - parenthèse fermante
        pass

    def test_mass_cleaning(self):
        #TODO
        # - test de juste plusieurs phrases dont certaines avec parenthèses
        pass
