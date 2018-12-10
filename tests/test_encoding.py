import unittest
import pyMorse.encoding as enc

class TestEncoding(unittest.TestCase):
    def test_constructor_w_sep(self):
        map = {"a": 1}
        sep = "A"
        e = enc.Encoding(map, sep)
        self.assertEqual(e.map, map)
        self.assertEqual(e.sep, sep)

    def test_constructor_no_sep(self):
        map = {"a": "1"}
        e = enc.Encoding(map)
        self.assertEqual(e.map, map)
        self.assertEqual(e.sep, '')

    def test__convert_match(self):
        e = enc.Encoding({"a": "1"})
        value = e._convert("a")
        self.assertEqual(value, "1")

    def test__convert_no_match(self):
        e = enc.Encoding({"a": "1"})
        with self.assertRaises(enc.InputNotRecognisedError):
            e._convert("A")

    def test_convert_fail(self):
        e = enc.Encoding({"a": "1"})
        with self.assertRaises(enc.InputNotRecognisedError):
            e.convert("aA")

    def test_convert(self):
        e = enc.Encoding({"a": "1", "b": "2"})
        value = e.convert("ab")
        self.assertEqual(value, "12")

    def test_morse_encoding(self):
        e = enc.MorseEncoding()
        self.assertEqual(e.convert("SOS"), "... --- ...")
        self.assertEqual(e.convert("CQ"), "-.-. --.-")
        self.assertEqual(e.convert("73"), "--... ...--")
        self.assertEqual(e.convert("Hello World"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
