import unittest
from pyMorse.converter.converter import Converter, InputNotRecognisedError
from pyMorse.converter.morse_converter import MorseConverter

class TestConverter(unittest.TestCase):
    def test_constructor(self):
        e = Converter()
        self.assertEqual(e.is_case, False)
        self.assertEqual(e.sep, '')
        self.assertEqual(e.enc, {})
        self.assertEqual(e.dec, {})

    def test__convert_match(self):
        m = {"a": "1"}
        e = Converter()
        value = e._convert("a", m)
        self.assertEqual(value, "1")

    def test__convert_no_match(self):
        m = {"a": "1"}
        e = Converter()
        with self.assertRaises(InputNotRecognisedError):
            e._convert("B", m)

    def test_encode_fail(self):
        e = Converter()
        with self.assertRaises(InputNotRecognisedError):
            e.encode("aA")

    def test_encode(self):
        e = Converter()
        e.enc = {"a": "1", "b": "2"}
        value = e.encode("aB")
        self.assertEqual(value, "12")

    def test_encode_insensitive(self):
        e = Converter(is_case_sensitive=True)
        e.enc = {"a": "1", "b": "2"}
        with self.assertRaises(InputNotRecognisedError):
            e.encode("aB")

    def test_decode_fail(self):
        e = Converter()
        with self.assertRaises(InputNotRecognisedError):
            e.decode("12")

    def test_decode_with_sep(self):
        e = Converter(letter_sep="|")
        e.dec = {"1": "a", "2": "b"}
        value = e.decode("1|2")
        self.assertEqual(value, "ab")

    def test_decode(self):
        e = Converter()
        e.dec = {"1": "a", "2": "b"}
        value = e.decode("12")
        self.assertEqual(value, "ab")

    def test__add_value_sensitive(self):
        e = Converter(is_case_sensitive=True)
        e._add_value("A", "b")
        self.assertEqual(e.enc, {"A": "b"})
        self.assertEqual(e.dec, {"b": "A"})

    def test__add_value_insensitive(self):
        e = Converter()
        e._add_value("A", "b")
        self.assertEqual(e.enc, {"a": "b"})
        self.assertEqual(e.dec, {"b": "a"})

    def test_encode_is_decode(self):
        e = Converter()
        e._add_value("a", "1")
        e._add_value("b", "2")
        self.assertEqual("ab", e.decode(e.encode("ab")))

    def test_morse_sample(self):
        e = MorseConverter()
        self.assertEqual(e.encode("SOS"), "... --- ...")
        self.assertEqual(e.encode("CQ"), "-.-. --.-")
        self.assertEqual(e.encode("73"), "--... ...--")
        self.assertEqual(e.encode("Hello World"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
