import unittest
from isurlshortener.unshortener import Unshortener
from isurlshortener.exceptions import ProtocolException, PathMissing


class TestUnshortener(unittest.TestCase):
    def test_unshorten_without_protocol(self):
        BIT_LY = 'bitly.is/1g3AhR6'
        with self.assertRaises(ProtocolException):
            Unshortener.unshorten_url(BIT_LY)

    def test_unshorten_with_invalid_protocol(self):
        sample_set = ['ftp://bit.ly/1G3AhR6']
        for sample in sample_set:
            with self.assertRaises(ProtocolException):
                Unshortener.unshorten_url(sample)

    def test_unshorten_without_path(self):
        sample_set = ['http://bitly.is/', 'http://bitly.is']

        for sample in sample_set:
            with self.assertRaises(PathMissing):
                Unshortener.unshorten_url(sample)

    def test_unshorten(self):
        sample_set = {'http://bit.ly/1ixYuRi': 'http://www.microsoft.com/'}

        for short_url, long_url in sample_set.items():
                self.assertEqual(long_url, Unshortener.unshorten_url(short_url))

    def test_unshorten_already_unshortened(self):
        sample_set = {'https://www.microsoft.com/de-de/': 'https://www.microsoft.com/de-de/'}

        for short_url, long_url in sample_set.items():
                self.assertEqual(long_url, Unshortener.unshorten_url(short_url))
