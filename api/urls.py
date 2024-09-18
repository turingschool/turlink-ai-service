from django.urls import path
from . import views
from .views import ping_view, generate_story

urlpatterns = [
    path('ping', ping_view, name='ping'),
    path('openai', generate_story, name='openai'),
]