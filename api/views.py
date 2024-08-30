from django.http import JsonResponse
from .client import ping

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

def test_view(request):
    url = "http://127.0.0.1:8000/test/"
    response = ping(url)
    return JsonResponse({"message": "This is a test endpoint"})