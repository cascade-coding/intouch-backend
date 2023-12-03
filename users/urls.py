from django.urls import path, include
from users import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('suggestions/', views.GetSuggestions.as_view()),
]