import unittest
from pyMorse.converter.morse_converter import MorseConverter

class TestMorseConverter(unittest.TestCase):
    def test_sample(self):
        e = MorseConverter()
        self.assertEqual(e.encode("SOS"), "... --- ...")
        self.assertEqual(e.encode("CQ"), "-.-. --.-")
        self.assertEqual(e.decode("--... ...--"), "73")
        self.assertEqual(e.decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "hello world")
