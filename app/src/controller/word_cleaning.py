import app.src.model.global_value as global_value

def purge_bad_char(word: str) -> str:
    """
        Remove all non-authorize char

        Parameter
        ---------
        word: str
            word to check

        Return
        ------
        word: str
            same word but without any non-authorize char
    """
    assert type(word) == str, "word is not a string"

    bad_char = global_value.Global_value().BAD_CHAR

    for chara in bad_char:
        while chara in word:
            assert len(word) > 1, f"CharacterError: a forbidden character have been found! PLease do not use '{word}' anymore."
            word = str(list(word).pop(list(word).index(chara)))

    return word

def punctuation(word: str) -> tuple:
    """
        Remove the punctuation at the end of a word

        Parameter
        ---------
        word: str
            word that contains a punctuation
        
        Return
        ------
        word: str
            word without punctuation

        punctuation: str
            the punctuation that was at the end of the word
    """
    assert type(word) == str, "word is not a string"
    assert word[-1] in global_value.Global_value().PUNCTUATION, "This word doesn't contain any punctuation."

    return word[:-1], word[-1]

def detection(word: str, nb_paren: int) -> tuple:
    """
        Assure that the word is correct and can be added to the database.
        In addition to the word, it can also return a punctuation

        Parameter
        ---------
        word: str
            word that need to be verify

        nb_paren: int
            number of opening parenthesis found

        Return
        ------
        nb_paren: intretour
            number of opening parenthesis found
        verified: str
            word cleansed of any unwanted character
        punctuation: ?str
            possible punctuation
    """
    verified = word
    gv = global_value.Global_value()

    for start in gv.PARENTHESIS_START:
        if start in verified:
            nb_paren += 1

    for end in gv.PARENTHESIS_END:
        if end in verified:
            nb_paren -= 1

    if nb_paren < 0:
        return nb_paren, None, None

    for chara in gv.BAD_CHAR:
        if chara in verified:
            verified = purge_bad_char(verified)
    
    for chara2 in gv.PUNCTUATION:
        if chara2 in verified:
            result = punctuation(verified)
            return nb_paren, result[0], result[1]
    
    return nb_paren, verified, None


def mass_cleaning(text: str) -> list:
    """
        Format a text for it to be ready to be saved in the database

        Parameter
        ---------
        text: str
            text that need to be formated

        Return
        ------
        formated: list<str>
            text cleanse and formatted in the format of a list of string
    """
    nb_parenthesis = 0

    text = text.split(" ")
    formated = []

    for word in text:
        test = detection(word, nb_parenthesis)
        nb_parenthesis = test[0]

        if test[1] is not None:
            # the space is added to allow words to be separate when the bot will talk
            formated.append(" "+test[1])

            if test[2] is not None:
                formated.append(test[2])

    return formated