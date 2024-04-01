class Mot:
    """
        Classe qui définit ce qu'est un mot

        Attribut
        --------
        valeur: str 
            text représentant le mot comme nous le voyons
        
        _listSuivant: list<list<int>>
            liste de liste de deux int
                - index d'un mot dans le dictionnaire courant
                - nombre de fois qu'il est apparu à la suite du mot actuel

        _dejaUtilise: list<int>
            liste des indexs déjà utilisés par ce mot pour la création de phrase.
    """

    def __init__(self, valeur: str) -> None:
        """
            Constructeur

            Paramètre
            ---------
            valeur: str
                mot comme nous le voyons
        """
        assert type(valeur) == str, "La valeur d'un mot doit être du String"
        self.valeur = valeur
        self._listSuivant = []
        self._dejaUtilise = []
    
    def ajoutMot(self, index: int) -> None:
        """
            Méthode qui ajouté un mot à _listSuivant
            si le mot y est déjà présent, il incrémente le nombre d'occurence

            Paramètre
            ---------
            index: int
                index du mot dans le dictionnaire courant
        """
        assert type(index) == int, "Index n'est pas un Int"

        trouve = False
        for i in range(len(self._listSuivant)):
            if self._listSuivant[i][0] == index:
                self._listSuivant[i][1] += 1
                trouve = True
                break
        
        if not trouve:
            self._listSuivant.append([index, 1])


    def _estFinPhrase(self, indexLeer: int) -> None:
        """
            Méthode qui uniquement lancé depuis le dictionnaire afin de spécifier que ce mot peut être utilisé comme fin de mot.

            Paramètre
            ---------
            indexLeer:  int
                Index du mot 'Leer' dans le dictionnaire courant
        """
        assert type(indexLeer) == int, "indexLeer n'est pas un int"
        assert self._listSuivant == [], "Cette méthode ne peut être utilisé qu'en cas d'initialisation."
        self._listSuivant.append([indexLeer, -1])


    def resetDejaUtilise(self) -> None:
        """
            Méthode qui permet de réinitialiser la liste des index déjà utiliser
            Cette méthode est utilisé lorsque que l'on commence à générer un nouveau texte.
        """
        self._dejaUtilise = []

    def getlistSuivant(self) -> None:
        """
            Méthode get qui permettra d'implémenter dans le dicitonnaire un algorithme qui permettra de trouver un chemin vers un mot particulier
        """
        return self._listSuivant

    def suivant(self) -> None:
        """
            Méthode qui permet de trouver le mot suivant le plus probable dans le cas d'une génération de phrase
        """
        choisi = [None, 0]

        for element in self._listSuivant:

            if element[1] > choisi[1] and (element[0] not in self._dejaUtilise or choisi == None):
                choisi = element

                if element[0] not in self._dejaUtilise:
                    self._dejaUtilise.append(element[0])
        
        if choisi[0] == None:
            choisi = self._listSuivant[0]

        return choisi[0]