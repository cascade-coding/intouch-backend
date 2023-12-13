from django.urls import path, include
from users import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('suggestions/', views.GetSuggestions.as_view()),
    path('add_new_post/', views.AddNewPostView.as_view()),
    path('home/posts/', views.GetHomePosts.as_view()),
    path('handle_following/', views.HandleFollowingView.as_view()),
    path('search_profile/<str:search>/', views.SearchProfileView.as_view()),
    path('activate_users/', views.ActivateUsersView.as_view()),
]
 