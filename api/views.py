from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .client import ping
from .openai import generate_story_from_openai  # Import the function

@api_view(['POST'])
def generate_story(request):
    """
    This view accepts a POST request with 'html_content' in the body
    and returns a summarized story using OpenAI API.
    """
    html_content = request.data.get('html_content', '')

    if not html_content:
        return Response({"error": "html_content is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Call the function from openai_service to generate the story
        story = generate_story_from_openai(html_content)
        return Response({"story": story}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def ping_view(request):
    url = "http://127.0.0.1:8000/ping/"
    
    try:
        response = ping(url)
        if isinstance(response, dict):
            return JsonResponse({"data": {"link": "www.example.com", "summary": "1. example 1\n2. example 2\n3. example 3"}}, status=200)
        else:
            return JsonResponse({"error": "Unexpected response type"}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
