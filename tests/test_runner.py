import unittest
from unittest import mock
from pyMorse.runner import Runner
from pyMorse.converter.converter import InputNotRecognisedError

class TestRunner(unittest.TestCase):
    @mock.patch('pyMorse.runner.Runner._output')
    @mock.patch('pyMorse.runner.Runner._input')
    def test_run_encode(self, i, o):
        i.side_effect = ["1", "SoS", "3"]
        r = Runner(0)
        r.run()
        o.assert_called_once_with("... --- ...")

    @mock.patch('pyMorse.runner.Runner._output')
    @mock.patch('pyMorse.runner.Runner._input')
    def test_run_decode(self, i, o):
        i.side_effect = ["2", "... --- ...", "n"]
        r = Runner(0)
        r.run()
        o.assert_called_once_with("sos")

    @mock.patch('pyMorse.runner.Runner._input')
    def test_run_encode_fail(self, i):
        i.side_effect = ["1", "...", "3"]
        r = Runner(0)
        with self.assertRaises(InputNotRecognisedError):
            r.run()

    @mock.patch('pyMorse.runner.Runner._input')
    def test_run_decode_fail(self, i):
        i.side_effect = ["2", "a", "n"]
        r = Runner(0)
        with self.assertRaises(InputNotRecognisedError):
            r.run()
