import unittest
from pyMorse.converter.substitute_converter import SubstituteConverter

class TestSubstituteConverter(unittest.TestCase):
    def test_sample(self):
        e = SubstituteConverter.simpleSub(3)
        self.assertEqual(e.encode("ABC"), "def")
        self.assertEqual(e.decode("def"), "abc")
        self.assertEqual(e.decode(e.encode("hu32 fdg")), "hu32 fdg")
