from django.urls import path
from . import views
from .views import ping_view, test_view

urlpatterns = [
    path('ping/', ping_view, name='ping'),
    path('test/', test_view, name='test'),
    path('parse/', views.HTMLParserView.as_view(), name='post'),
]