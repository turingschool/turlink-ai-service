import unittest
from unittest.mock import patch, MagicMock
#from story_generator import generate_story, format_response, get_short_story

class StoryGeneratorTest(unittest.TestCase):
    @patch('story_generator.client.chat.completions.create')
    def test_generate_story(self, mock_openai_api):
        # Set up the mock response from the OpenAI API
        mock_openai_api.return_value = {
            "choices": [{
                "message": {
                    "content": "- Bullet 1\n- Bullet 2\n- Bullet 3"
                }
            }]
        }

        # Test input
        words = "Once upon a time in a faraway land, there was a brave knight."

        # Call the function we are testing
        #story = generate_story(words)

        # Assert that the story is returned correctly
        expected_story = "- Bullet 1\n- Bullet 2\n- Bullet 3"
        #self.assertEqual(story, expected_story)

        # Check if the OpenAI API was called with the correct parameters
        mock_openai_api.assert_called_once_with(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"""You are a helpful assistant.
                Summarize the following content: {words}.
                Use 3 bullet points."""
            }],
            temperature=0.8,
            max_tokens=100
        )

if __name__ == "__main__":
    unittest.main()