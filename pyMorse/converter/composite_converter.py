from pyMorse.converter.converter import Converter

class CompositeConverter(Converter):
    """This represents the conversion of characters using multiple converters.

    Args:
        converters(:obj:`list` of :obj:`Converter`): List of converts to be applied (in order for encoding).
    """
    def __init__(self, converters):
        self.converters = converters

    def encode(self, text):
        ret_val = text
        for c in self.converters:
            ret_val = c.encode(ret_val)
        return ret_val

    def decode(self, text):
        ret_val = text
        for c in reversed(self.converters):
            ret_val = c.decode(ret_val)
        return ret_val
