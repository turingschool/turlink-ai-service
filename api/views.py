from django.shortcuts import get_object_or_404
import json
from .models import Event, Attendee
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
# Create your views here.

@csrf_exempt
def create_summary(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        model = data.get('gpt-3.5-turbo')
        max_tokens = data.get('100')
        role = data[messages][0][role].get('user')
        content = data[messages][0][content].get('user')


        return JsonResponse({
            'data': {
                'model': model,
                'max_tokens': max_tokens,
                'messages': [
                    {
                        'role': role,
                        'content': content,
                    }
                ]
            }
        })
    