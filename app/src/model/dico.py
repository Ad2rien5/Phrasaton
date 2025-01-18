import app.src.model.global_value as global_value
import app.src.model.word as word


class Dico:
    """
    Stock and manipulate words

    Attributes
    ----------
    nbSentences: int
        Number of sentence contained by the previous user's message.
        It allows to create a response with the same amount of sentence.

    words: list<Word>
        list of words
        At creation, generate some essential words from "global_value.py"
    """

    def __init__(self) -> None:
        self.nbSentences = 0

        # initialisation de la base de donnée
        self.gv = global_value.GlobalValue()
        self.words = [word.Word(element) for element in self.gv.PUNCTUATION]
        self.words.append(word.Word("leer"))
        for index in self.gv.SENTENCE_END:
            self.words[index].is_end(self.gv.get_index_leer())

    def find(self, value: str) -> int:
        """
        Find the index of a given word

        Parameter
        ---------
        value: str
            wanted word

        Return
        ------
        index: int
            index of the word inside the dictionary
            return -1 if the word isn't find
        """
        assert type(value) == str, "value is not a string"
        for i in range(len(self.words)):
            if self.words[i].value == value:
                return i
        return -1

    def add_occurrence(self, actual: str, after: str) -> None:
        """
        Add an occurrence of the "next" word in the "actual" word

        Parameters
        ----------
        actual: str
            word that need to add an occurrence

        after: str
            the occurrence
        """
        assert type(actual) == str, "actual is not a string"
        assert type(after) == str, "next is not a string"

        index1 = self.find(actual)
        if index1 == -1:
            self.words.append(word.Word(actual))
            index1 = len(self.words) - 1

        index2 = self.find(after)
        if index2 == -1:
            self.words.append(word.Word(after))
            index2 = len(self.words) - 1

        self.words[index1].add_word(index2)

    def reset_cache(self) -> None:
        """
        Méthode qui va permettre de réinitialiser pour tous les mots, leur attribut 'dejaUtilise' (voir './Mot.py')
        Reset all cache from each word
        """
        for i in range(len(self.words)):
            self.words[i].delete_cache()

    def speak(self) -> str:
        """
        Generate a text

        Return
        ------
        text: str
            generated text
        """
        assert self.nbSentences != 0, "Phrasaton speak only after the user."
        assert len(self.words) > 6, "No words are actually known!"
        current = 3
        nb = 0
        text = ""

        while nb < self.nbSentences:

            after = self.words[current].next_word()
            text += self.words[after].value

            if self.words[after].value in self.gv.end_sent_str():
                nb += 1

            current = after

        self.reset_cache()
        return text

    def learn(self, texte: tuple) -> None:
        """
        Save a whole text in the database

        Parameter
        ---------
        text: str
            Text that need to be saved
        """
        # counting the sentences
        self.nbSentences = 0
        
        for punct in texte:
            if punct in self.gv.end_sent_str():
                self.nbSentences += 1

        assert (
            texte[-1] in self.gv.end_sent_str()
        ), "This sentence don't end with a valid punctuation."

        # add the first word of the text to all ending punctuation
        for punctuation in self.gv.end_sent_str():
            self.add_occurrence(punctuation, texte[0])

        for index in range(len(texte[1:])):
            self.add_occurrence(texte[index], texte[index + 1])
