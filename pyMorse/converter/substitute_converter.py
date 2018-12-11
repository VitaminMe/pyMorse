from pyMorse.converter.converter import Converter

class SubstituteConverter(Converter):
    """This represents the encoding of characters into other characters using
    a shift number.

    Args:
        shift(int): Number of letters to shift by (e.g. 1 means A becomes B).
        characters(list): List of characters to be shifted into itself.
        is_case_sensitive(bool): Indicates if 'a' != 'A' (defaults to false).
    """
    def __init__(self, shift, characters, is_case_sensitive=False):
        super().__init__(is_case_sensitive=is_case_sensitive)
        for idx, c in enumerate(characters):
            super()._add_value(c, characters[(idx + shift) % len(characters) ])

    @staticmethod
    def simpleSub(shift=3):
        return SubstituteConverter(shift, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
