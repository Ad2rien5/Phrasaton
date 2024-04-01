class Global_value:
    """
        Global_value
        ------------
        BAD_CHAR: list<str>
            List which contain forbidden character.

        PARENTHESIS_START: list<str>
            List which contain all types of starting parenthesis.

        PARENTHESIS_END: list<str>
            List which contain all types of ending parenthesis.

        PUNCTUATION: list<str>
            List which contain all punctuation that is not forbidden.
        
        SENTENCE_END: list<str>


    """

    def __init__(self) -> None:    
        self.BAD_CHAR = ["\"", "<", ">", "/", "\\", "_", "卐"] #il faudra rajouter les << et >>
        self.PARENTHESIS_START = ["(", "{", "["]
        self.PARENTHESIS_END = [")", "}",  "]"]
        self.PUNCTUATION = ["?", ",", ";", ".", ":", "!"]
        self.SENTENCE_END = [0, 3, 5]
        
        
    def SENT_END_STR(self) -> list:
        """
        Return a list of the value of 'self.SENTENCE_END' but in str type. 
        """
        return [self.PUNCTUATION[i] for i in self.SENTENCE_END]