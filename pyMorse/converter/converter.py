class Converter:
    """This represents the two-way conversion characters.

    Args:
        is_case_sensitive(:obj:`bool`, optional): Indicates if 'a' != 'A' (defaults to false)
        letter_sep(:obj:`str`, optional): String that seperates each encoded value (defaults to '')
    """
    def __init__(self, is_case_sensitive=False, letter_sep=""):
        self.enc = {}
        self.dec = {}
        self.is_case = is_case_sensitive
        self.sep = letter_sep

    def _add_value(self, normal, encoded):
        if self.is_case:
            self.enc[normal] = encoded
            self.dec[encoded] = normal
        else:
            self.enc[normal.lower()] = encoded.lower()
            self.dec[encoded.lower()] = normal.lower()

    def encode(self, text):
        """This converts text into encoded value

        Args:
            text(str): String to be encoded

        Raises:
            InputNotRecognisedError: If text contains character that cannot be converted
        """
        return self.sep.join(map(lambda c: self._convert(c, self.enc), list(text)))

    def decode(self, text):
        """This converts encoded value into text

        Args:
            text(str): String to be decoded

        Raises:
            InputNotRecognisedError: If text contains character that cannot be converted
        """
        if self.sep:
            return ''.join(map(lambda c: self._convert(c, self.dec), text.split(self.sep)))
        return ''.join(map(lambda c: self._convert(c, self.dec), list(text)))

    def _convert(self, c, map):
        if self.is_case:
            ret_val = map.get(c, None)
        else:
            ret_val = map.get(c.lower(), None)
        if ret_val:
            return ret_val
        raise InputNotRecognisedError()

class InputNotRecognisedError(Exception):
    pass
