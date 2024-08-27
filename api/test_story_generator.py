import unittest
from unittest.mock import patch, MagicMock
from story_generator import generate_story

class TestStoryGenerator(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/"
    
    @patch("client.generate_story")
    def test_generate_story(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        
        link = "example link or beautiful_soup html files"
        system_prompt = f"""You are a a helpful assistant.
        Summarize the following content: {link}.
        Use 3 bullet points."""

        mock_response.json.return_value = { "messages": [{ "role": "user", "content": system_prompt}] }
        mock_requests.post.return_value = mock_response

        status, response = generate_story(self.url)
        self.assertTrue(status)
        self.assertEqual(response["messages"], [{ "role": "user", "content": system_prompt}])
        self.assertEqual(response["messages"][0]["role"], "user")
        self.assertEqual(response["messages"][0]["content"], system_prompt)


if __name__ == "__main__":
    unittest.main()