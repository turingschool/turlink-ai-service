import unittest
from unittest.mock import patch, MagicMock
from client import ping

class TestClient(unittest.TestCase):
    def setUp(self):
        self.url = "https://api.service.com"

    @patch("client.requests")
    def test_ping_returns_200(self, mock_requests):
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "ok"}
        mock_requests.get.return_value = mock_response

        status, body = ping(self.url)
        self.assertTrue(status)
        self.assertEqual(body["status"], "ok")

        # result = ping(self.url)

    @patch("client.requests")
    def test_ping_returns_500(self, mock_requests):
        
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_requests.get.return_value = mock_response

        status, body = ping(self.url)
        # result = ping(self.url)
        self.assertFalse(status)

if __name__ == "__main__":
    unittest.main()