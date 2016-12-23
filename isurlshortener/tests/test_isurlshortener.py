import unittest
from isurlshortener.isurlshortener import IsUrlShortener


class TestIsUrlShortener(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(IsUrlShortener.is_url_shortener(''), 'Empty string error')

    def test_bitly_url(self):
        HTTPS_BIT_LY = 'https://bitly.is/1g3AhR6'
        self.assertTrue(IsUrlShortener.is_url_shortener(HTTPS_BIT_LY),
                        'Bit.ly not detected "{}"'.format(HTTPS_BIT_LY))

    def test_bitly_url_without_http_prefix(self):
        BIT_LY = 'bitly.is/1g3AhR6'
        self.assertTrue(IsUrlShortener.is_url_shortener(BIT_LY),
                        'Bit.ly not detected "{}"'.format(BIT_LY))

    def test_no_shortener(self):
        GOOGLE = 'https://www.google.com'
        self.assertFalse(IsUrlShortener.is_url_shortener(GOOGLE),
                         'Detected {} as shortener'.format(GOOGLE))

    def test_former_url_shortener(self):
        expected = {'bitly.is/1g3AhR6': False, 'fur.ly/1g3AhR6': True}

        for k, v in expected.items():
            self.assertEqual(v, IsUrlShortener.is_disabled_url_shortener(k),
                             'Error for {}'.format(k))

    def test_is_or_was_shortener(self):
        expected = {'bitly.is/1g3AhR6': True,
                    'fur.ly/1g3AhR6': True,
                    'www.google.com': False}

        for k, v in expected.items():
            self.assertEqual(v, IsUrlShortener.is_or_was_from_url_shortener(k),
                             'Error for {}'.format(k))

    def test_raises_assertion_on_missing_data(self):
        BIT_LY = 'bitly.is/1g3AhR6'
        with self.assertRaises(FileNotFoundError):
            IsUrlShortener._is_in_servicelist(BIT_LY, 'this_file_does_not_exist')
