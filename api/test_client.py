import unittest
from unittest.mock import patch, MagicMock
#from story_generator import generate_story
from client import ping

class TestClient(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/"
    
    @patch("client.ping")
    def test_ping(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        system_prompt = "1. example 1\n2. example 2\n3. example 3"

        mock_response.json.return_value = { "data": {"link": "www.example.com", "summary": system_prompt} }
        mock_requests.get.return_value = mock_response

        response = mock_response.json()
    
        self.assertEqual(response["data"]["link"], "www.example.com")
        self.assertEqual(response["data"]["summary"], system_prompt)

if __name__ == "__main__":
    unittest.main()