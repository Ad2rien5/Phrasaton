class Word:
    """
        Attribute
        --------
        value: str 
            The word as we can see it.
        
        next_list: list<list<int>>
            list of list of two int
                - index of the word in the actual dictionary
                - number of times it has appeared after the current word

        already_use: list<int>
            list of index of 'next_list' pointing to word that already have been use in the current sentence.
    """

    def __init__(self, value: str) -> None:
        self.value = value
        self._next = []
        self._already_use = []
    
    def add_word(self, index: int) -> None:
        """
            Add a word to the 'next_list', but if the word is already in it, it incremente the number of encounter.
        """
        fund = False
        for i in range(len(self._next_list)):
            if self._next[i][0] == index:
                self._next[i][1] += 1
                fund = True
                break
        
        if not fund:
            self._next.append([index, 1])


    def is_end(self, indexLeer: int) -> None:
        """
            Function that specifie that the current word can be use as the end of a sentence.
        """
        assert not self._next, "This function can only be use just after it's initialisation."
        self._next.append([indexLeer, -1])


    def reset_already(self) -> None:
        """
            Méthode qui permet de réinitialiser la liste des index déjà utiliser
            Cette méthode est utilisé lorsque que l'on commence à générer un nouveau texte.
        """
        self._already_use = []

    def next_word(self) -> int:
        """
            Function that find the next word in the sentence (in the case of the generation of a sentence).

            Return
            ------
            choosen_one: int
                index of the next word in the dictionary
        """
        choosen_one = [None, 0]

        for element in self._next:

            if element[1] > choosen_one[1] and (element[0] not in self._already_use or choosen_one == None):
                choosen_one = element

                if element[0] not in self._already_use:
                    self._already_use.append(element[0])
        
        if choosen_one[0] == None:
            return self._next[0][0]

        return choosen_one[0]