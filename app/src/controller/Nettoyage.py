import global_value as global_value

def antiMauvaisSigne(mot: str) -> str:
    """
        Fonction qui va épurrer un mot de tout mauvais signe

        Paramètre
        ---------
        mot: str
            mot à controller

        Sortie
        ------
        mot: str
            mot épurré
    """
    assert type(mot) == str, "mot n'est pas un string"

    for chara in global_value.MAUVAIS_SIGNE:
        while chara in mot:
            assert len(mot) > 1, f"CharacterError: a forbidden character have been found! PLease do not use '{mot}' anymore."
            mot = str(list(mot).pop(list(mot).index(chara)))

    return mot

def ponctuation(mot: str) -> tuple:
    """
        Fonction qui permet de supprimer la ponctuation à la fin d'un mot

        Paramètre
        ---------
        mot: str
            mot à manipuler
        
        Sortie
        ------
        mot: str
            mot sans ponctuation
        ponctuation: str
            ponctuation qui était à la fin du mot
    """
    assert type(mot) == str, "mot n'est pas un string"
    assert mot[-1] in global_value.PONCTUATION, "aucune raison d'appeler cette fonction"

    return mot[:-1], mot[-1]

def detection(mot: str, nb_paren: int) -> tuple: 
    """
        Fonction qui permet de s'assurer qu'un mot est apte à être ajouter à la base de donné.
        Peut aussi renvoyer un signe de ponctuation

        Paramètre
        ---------
        mot: str
            mot que l'on souhaite vérifier

        nb_paren: int
            nombre d'ouverture de parenthèse rencontrées moins les fermetures rencontrées

        Sortie
        ------
        nb_paren: int
            renvoie de la valeur à la fonction mère
        retour: str
            mot nettoyé de toute symbole nuisible
        ponctuation: ?str
            éventuelle ponctuation qui était collé au mot
    """
    retour = mot

    for debut in global_value.DEBUT_PARENTHESE:
        if debut in retour:
            nb_paren += 1

    for fin in global_value.FIN_PARENTHESE:
        if fin in retour:
            nb_paren -= 1

    if nb_paren > 0:
        return nb_paren, None, None

    for chara in global_value.MAUVAIS_SIGNE:
        if chara in retour:
            retour = antiMauvaisSigne(retour)[0]
    
    for chara2 in global_value.PONCTUATION:
        if chara2 in retour:
            result = ponctuation(retour)
            return nb_paren, result[0], result[1]
    
    return nb_paren, retour, None


def Nettoyage_de_Masse(texte: str) -> list:
    """
        Fonction qui va formater un texte pour qu'il soit prêt à être rangé dans la Base de Donnée

        Paramètre
        ---------
        texte: str
            Texte que l'on souhaite formater

        Sortie
        ------
        formate: list<str>
            texte formaté et nettoyé sous forme de liste de string
    """
    # TODO implémentation du sujet de la question

    # Nombre d'ouverture de parenthèse rencontrées moins les fermetures rencontrées
    nb_parenthese = 0

    texte = texte.split(" ")
    formate = []

    for mot in texte:
        test = detection(mot, nb_parenthese)
        nb_parenthese = test[0]

        if test[1] != None :
            # l'espace ajouté permet de séparer les mots d'un espace quand il faudra parler
            formate.append(" "+test[1])

            if test[2] != None:
                formate.append(test[2])

    return formate