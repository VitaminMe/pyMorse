from pyMorse.converter.converter import Converter

class MorseConverter(Converter):
    """This represents the encoding of characters into Morse code.

    Note - Both ' ' and '/' represent a 3 interval (3 dots) of silence.  The latter
    is used to visually distinguish words.
    """
    def __init__(self):
        super().__init__(letter_sep=" ")
        super()._add_value("a", ".-")
        super()._add_value("b", "-...")
        super()._add_value("c", "-.-.")
        super()._add_value("d", "-..")
        super()._add_value("e", ".")
        super()._add_value("f", "..-.")
        super()._add_value("g", "--.")
        super()._add_value("h", "....")
        super()._add_value("i", "..")
        super()._add_value("j", ".---")
        super()._add_value("k", "-.-")
        super()._add_value("l", ".-..")
        super()._add_value("m", "--")
        super()._add_value("n", "-.")
        super()._add_value("o", "---")
        super()._add_value("p", ".--.")
        super()._add_value("q", "--.-")
        super()._add_value("r", ".-.")
        super()._add_value("s", "...")
        super()._add_value("t", "-")
        super()._add_value("u", "..-")
        super()._add_value("v", "...-")
        super()._add_value("w", ".--")
        super()._add_value("x", "-..-")
        super()._add_value("y", "-.--")
        super()._add_value("z", "--..")
        super()._add_value("0", "-----")
        super()._add_value("1", ".----")
        super()._add_value("2", "..---")
        super()._add_value("3", "...--")
        super()._add_value("4", "....-")
        super()._add_value("5", ".....")
        super()._add_value("6", "-....")
        super()._add_value("7", "--...")
        super()._add_value("8", "---..")
        super()._add_value("9", "----.")
        super()._add_value(" ", "/")
