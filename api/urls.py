from django.urls import path
from . import views

urlpatterns = [
    path('ai/', views.create_summary, name='create_summary')
]