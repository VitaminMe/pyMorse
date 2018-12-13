import unittest
from unittest import mock
from pyMorse.converter.converter import Converter
from pyMorse.converter.composite_converter import CompositeConverter

class TestCompositeConverter(unittest.TestCase):
    def test_encode_empty(self):
        e = CompositeConverter([])
        self.assertEqual(e.encode("text"), "text")

    def test_decode_empty(self):
        e = CompositeConverter([])
        self.assertEqual(e.decode("text"), "text")

    @mock.patch('pyMorse.converter.composite_converter.Converter.encode')
    def test_encode(self, encode):
        encode.side_effect = ["AAAA", "bbbb"]
        e = CompositeConverter([Converter(), Converter()])

        self.assertEqual(e.encode("text"), "bbbb")
        encode.assert_has_calls([
            mock.call("text"),
            mock.call("AAAA")
        ])

    @mock.patch('pyMorse.converter.composite_converter.Converter.decode')
    def test_decode(self, decode):
        decode.side_effect = ["AAAA", "bbbb"]
        e = CompositeConverter([Converter(), Converter()])

        self.assertEqual(e.decode("text"), "bbbb")
        decode.assert_has_calls([
            mock.call("text"),
            mock.call("AAAA")
        ])
