class Encoding:
    """This represents an encoding of characters.

    Args:
        map(dict): Maps characters on to their encoded value.
        letter_sep(str): String that seperates each encoded value (defaults to '')
    """
    def __init__(self, map, letter_sep=''):
        self.map = map
        self.sep = letter_sep

    def convert(self, text):
        """This converts text into encoded value

        Args:
            text(str): String to be encoded

        Raises:
            InputNotRecognisedError: If text contains character that cannot be converted
        """
        return self.sep.join(map(lambda c: self._convert(c), list(text)))

    def _convert(self, c):
        ret_val = self.map.get(c, None)
        if ret_val:
            return ret_val
        raise InputNotRecognisedError()

class InputNotRecognisedError(Exception):
    pass

class MorseEncoding(Encoding):
    """This represents the encoding of characters into Morse code.

    Note - Both ' ' and '/' represent a 3 interval (3 dots) of silence.  The latter
    is used to visually distinguish words.
    """
    def __init__(self):
        super().__init__({
            "a": ".-", "A": ".-",
            "b": "-...", "B": "-...",
            "c": "-.-.", "C": "-.-.",
            "d": "-..", "D": "-..",
            "e": ".", "E": ".",
            "f": "..-.", "F": "..-.",
            "g": "--.", "G": "--.",
            "h": "....", "H": "....",
            "i": "..", "I": "..",
            "j": ".---", "J": ".---",
            "k": "-.-", "K": "-.-",
            "l": ".-..", "L": ".-..",
            "m": "--", "M": "--",
            "n": "-.", "N": "-.",
            "o": "---", "O": "---",
            "p": ".--.", "P": ".--.",
            "q": "--.-", "Q": "--.-",
            "r": ".-.", "R": ".-.",
            "s": "...", "S": "...",
            "t": "-", "T": "-",
            "u": "..-", "U": "..-",
            "v": "...-", "V": "...-",
            "w": ".--", "W": ".--",
            "x": "-..-", "X": "-..-",
            "y": "-.--", "Y": "-.--",
            "z": "--..", "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            " ": "/"
        }, " ")
