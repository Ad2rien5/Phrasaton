"""
    Constante
    ---------
    MAUVAIS_SIGNE: list<string>
        Liste qui contient les caractères interdits.
        Le cas des différents types de parenthèse sont pris à part

    DEBUT_PARENTHESE: list<string>
        List des ouvertures des différents types de parenthèse
    
    FIN_PARENTHESE: list<string>
        Liste des fermetures des différents types de parenthèse

    PONCTUATION: list<string>
        Liste des différents caratères servant de ponctuation
    
    FIN_PHRASE: list<int>
        liste des indexs des caratères servant à finir une phrase
    
    FIN_PHRASE_STR: list<str>
        liste FIN_PHRASE mais tous les indexs ont été converti en str de puis la liste PONCTUATION
"""

MAUVAIS_SIGNE = ["\"", "<", ">", "/", "\\", "_", "卐"] #il faudra rajouter les << et >>
DEBUT_PARENTHESE = ["(", "{", "["]
FIN_PARENTHESE = [")", "}",  "]"]
PONCTUATION = ["?", ",", ";", ".", ":", "!"]
FIN_PHRASE = [0, 3, 5]
FIN_PHRASE_STR = [PONCTUATION[i] for i in FIN_PHRASE]