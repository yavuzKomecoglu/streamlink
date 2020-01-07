import unittest

from streamlink.plugins.fenerbahcetv import FenerbahceTV


class TestPluginFoxTR(unittest.TestCase):
    def test_can_handle_url(self):
        should_match = [
            'https://www.fenerbahce.org/fbtv/',
        ]
        for url in should_match:
            self.assertTrue(FenerbahceTV.can_handle_url(url))

    def test_can_handle_url_negative(self):
        should_not_match = [
            'https://example.com/index.html',
        ]
        for url in should_not_match:
            self.assertFalse(FenerbahceTV.can_handle_url(url))
