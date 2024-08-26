import unittest
from unittest.mock import patch, MagicMock
from client import ping

class TestClient(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/"
    
    @patch("client.requests")
    def test_ping(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = { "messages": [{ "role": "user", "content": "What is AI"}] }
        mock_requests.post.return_value = mock_response
        
        status, response = ping(self.url)
        self.assertTrue(status)
        self.assertEqual(response["messages"], [{ "role": "user", "content": "What is AI"}])
        self.assertEqual(response["messages"][0]["role"], "user")
        self.assertEqual(response["messages"][0]["content"], "What is AI")

if __name__ == "__main__":
    unittest.main()