from django.http import JsonResponse, HttpResponseBadRequest
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .serializers import SummarySerializer
# Create your views here.

@csrf_exempt
def create_summary(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON')
    
        serializer = SummarySerializer(data=data)
        if serializer.is_valid():
            valid_data = serializer.validated_data

            return JsonResponse({
                'data': valid_data
            })
        else:
            return HttpResponseBadRequest('Invalid data')
        
    return HttpResponseBadRequest('Invalid request method')
            
