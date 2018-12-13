from pyMorse.converter.morse_converter import MorseConverter
from pyMorse.converter.substitute_converter import SubstituteConverter
from pyMorse.converter.composite_converter import CompositeConverter
from pyMorse.converter.morse_converter import MorseConverter

class Runner:
    """This class handles running the converter interactively using console.

    Args:
        shift(int): Shift to be used for encoding/decoding
    """
    def __init__(self, shift=5):
        self.converter = CompositeConverter([SubstituteConverter.simpleSub(shift), MorseConverter()])
        # Store text messages to make testing easier and simpler to replace
        self.choose_msg = "Choose option:\n1. Encode\n2. Decode\n*. Exit\n"
        self.enter_enc = "Enter text to encode: "
        self.enter_dec = "Enter morse to decode: "

    def run(self):
        "Simple TUI to enable encode and decode interactively"
        should_run = True
        while should_run:
            resp=self._input(self.choose_msg).strip()
            # Encode and decode can raise error - unhandled so don't enter invalid data ;-)
            if resp == "1":
                self._output(self.converter.encode(self._input(self.enter_enc)))
            elif resp == "2":
                self._output(self.converter.decode(self._input(self.enter_dec)))
            else:
                should_run = False

    def _output(self, o):
        print(o)

    def _input(self, o):
        return input(o)
