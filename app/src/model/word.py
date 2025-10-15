class Word:
    """
    Attribute
    --------
    value: str
        The word as we can see it.

    next_list: list<list<int>>
        list of multiple list of two int
            - index of the word in the actual dictionary
            - number of times it has appeared after the current word

    cache: list<int>
        list of index of 'next_list' pointing to word that already have been use in the current sentence.
    """

    def __init__(self, value: str) -> None:
        self.value : str = value
        self._next : list[list] = []
        self._cache : list[int] = []

    def add_word(self, index: int) -> None:
        """
        Add a word to the 'next_list', but if the word is already in it, it increments the number of encounter.

        Parameter :
        -----------
        index: int
            The index of the word to be added.
        """
        for i in range(len(self._next)):
            if self._next[i][0] == index:
                self._next[i][1] += 1
                return
        self._next.append([index, 1])

    def is_end(self, index_leer: int) -> None:
        """
        Function that specify that the current word can be used as the end of a sentence.
        """
        assert (
            not self._next
        ), "This function can only be use just after it's initialisation."
        self._next.append([index_leer, -1])

    def delete_cache(self) -> None:
        """
        Delete all previous use of this word
        """
        self._cache = []

    def next_word(self) -> int:
        """
        Function that find the next word in the sentence (in the case of the generation of a sentence).

        Return
        ------
        chosen_one: int
            index of the next word in the dictionary
        """
        assert len(self._next) > 0, f"Can't ask a word for next when it has no next {self.value}"
        chosen_one : list[int]|None = None

        for element in self._next:

            if chosen_one is None or (
                element[1] >= chosen_one[1] and element[0] not in self._cache
            ):
                chosen_one = element

        self._cache.append(chosen_one[0])
        return chosen_one[0]
