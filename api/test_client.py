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
        
        link = "example link or beautiful_soup html files"
        system_prompt = f"""You are a a helpful assistant.
        Summarize the following content: {link}.
        Use 3 bullet points."""

        mock_response.json.return_value = { "data": [{"messages": { "role": "user", "content": system_prompt}}] }
        mock_requests.get.return_value = mock_response

        response = mock_response.json()
    
        self.assertEqual(response["data"][0]["messages"]["role"], "user")
        self.assertEqual(response["data"][0]["messages"]["content"], system_prompt)


if __name__ == "__main__":
    unittest.main()