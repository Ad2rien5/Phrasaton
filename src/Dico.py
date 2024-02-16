from Mot import *
import Constante
import Nettoyage

class Dico:
    """
        Classe qui permet de stocker et manipuler des mots

        Attribut
        --------
        nbPhrase: int
            Nombre de phrase que le précédent message de l'utilisateur contient
            Cela permet de lui générer un message contenant le même nombre de phrase

        mots: list<Mot>
            liste des mots que contient ce dictionnnaire
    """

    def __init__(self) -> None:
        """
            Constructeur

            Attention
            ---------
            Génère les premiers éléments essentiels de la variable 'mots' depuis les constantes du fichier './Constante.py'
        """
        self.nbPhrase = 0

        # initialisation de la base de donnée
        self.mots = [Mot(element) for element in Constante.PONCTUATION]
        self.mots.append(Mot("leer"))
        for index in Constante.FIN_PHRASE:
            self.mots[index]._estFinPhrase(6)

    
    def est_present(self, valeur: str) -> int:
        """
            Méthode qui permet de chercher un mot dans le dictionnaire à partir du texte

            Paramètre
            ---------
            valeur: str
                mot comme nous le voyons
            
            Sortie
            ------
            index: int
                index du mot rechercher dans le dictionnaire
                retourne -1 si le mot ne se trouve pas dans le dictionnaire
        """
        assert type(valeur) == str, "valeur n'est pas un string"
        for i in range(len(self.mots)):
            if (self.mots[i].valeur == valeur):
                return i
        return -1
    

    def ajoutProba(self, present: str, suivant: str) -> None:
        """
            Méthode qui permet d'ajouter un mot dans la listeSuivant d'un autre (voir './Mot.py')

            Paramètre
            ---------
            present: str
                mot qui doit ajouter un autre

            suivant: str
                mot qui doit être ajouté
        """
        assert type(present) == str, "present n'est pas un string"
        assert type(present) == str, "suivant n'est pas un string"

        index1 = self.est_present(present)
        if (index1 == -1):
            self.mots.append(Mot(present))
            index1 = len(self.mots) - 1

        index2 = self.est_present(suivant)
        if (index2 == -1):
            self.mots.append(Mot(suivant))
            index2 = len(self.mots) - 1

        self.mots[index1].ajoutMot(index2)

        #print(f"{present} \n {self.mots[index1].getlistSuivant()}\n\n")

    
    def reinitDejaUtilise(self) -> None:
        """
            Méthode qui va permettre de réinitialiser pour tous les mots, leur attribut 'dejaUtilise' (voir './Mot.py')
        """
        for i in range(len(self.mots)):
            self.mots[i].resetDejaUtilise()
    

    def parle(self, sujet: str = None) -> str:
        """
            Méthode qui va générer un texte

            Paramètre
            ---------
            sujet: ?str
                Sujet que l'une des phrases générer doit mentionner
                est nul par défaut

            Sortie
            ------
            texte: str
                texte généré 
        """
        # TODO l'utilisation de 'sujet' est à implémenter plus tard
        if sujet != None:
            assert type(sujet) == str, "Le sujet n'est pas un string"
        assert self.nbPhrase != 0, "L'IA ne parle qu'après l'utilisateur."
        assert len(self.mots) > 6, "L'IA ne connait pas de mot."
        current = 3
        nb = 0
        texte = ""

        while nb < self.nbPhrase:
            
            suivant = self.mots[current].suivant()
            texte += self.mots[suivant].valeur

            if self.mots[suivant].valeur in Constante.FIN_PHRASE_STR:
                nb += 1

            current = suivant

        self.reinitDejaUtilise()
        return texte
    

    def apprends(self, texte: str) -> None:
        """
            Fonction qui va enregistrer toute un texte dans une base de donnée

            Paramètre
            ---------
            texte: str
                Texte que l'on souhaite ajouter dans la base de donnée
        """
        propre = Nettoyage.Nettoyage_de_Masse(texte)

        # on compte le nombre de phrase
        self.nbPhrase = 0
        for ponct in propre:
            if ponct in Constante.FIN_PHRASE_STR:
                self.nbPhrase += 1

        assert propre[-1] in Constante.FIN_PHRASE_STR, "Cette phrase ne se termine pas par un signe de ponctuation valide!"
        
        # ajout du premier mot à la liste des suivants de tous les signes de ponctuation
        for ponctuation in Constante.FIN_PHRASE_STR:
            self.ajoutProba(ponctuation, propre[0])

        for mot in range(len(propre[1:])):
            self.ajoutProba(propre[mot], propre[mot+1])

    
    def trouverSujet(texte: list) -> list:
        """
            Méthode qui va chercher le sujet de chaque phrase du texte envoyer par l'utilisateur

            Paramètre
            ---------
            texte: list<str>
                liste des différents mots dans le bon ordre composant le texte envoyé par l'utilisateur
            
            Sortie
            ------
            sujets: list<str>
                liste des mots 'sujet' de chaque phrase (dans le bon ordre)
        """
        sujets = []
        # on commence par séparer les différentes phrases dans texte

        # on vérifie que le nombre de phrase trouvé corresponde avec nbPhrase

        # on cherche pour chaque phrase le string le plus long

        #on retourne
        return sujets
