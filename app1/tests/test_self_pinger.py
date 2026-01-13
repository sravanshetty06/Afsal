from unittest import mock
from django.test import TestCase
from django.conf import settings

from app1 import self_pinger


class SelfPingerTests(TestCase):
    def test_ping_once_success(self):
        settings.RENDER_SELF_URL = 'https://afsal.onrender.com'
        mock_resp = mock.Mock()
        mock_resp.status_code = 200
        with mock.patch('app1.self_pinger.requests.get', return_value=mock_resp) as mocked_get:
            status = self_pinger.ping_once()
            mocked_get.assert_called_once_with(settings.RENDER_SELF_URL, timeout=10)
            self.assertEqual(status, 200)

    def test_ping_once_exception(self):
        settings.RENDER_SELF_URL = 'https://afsal.onrender.com'
        with mock.patch('app1.self_pinger.requests.get', side_effect=Exception("boom")) as mocked_get:
            status = self_pinger.ping_once()
            mocked_get.assert_called_once()
            self.assertIsNone(status)
