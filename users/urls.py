from django.urls import path, include
from users import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('suggestions/', views.GetSuggestionsView.as_view()),
    path('add_new_post/', views.AddNewPostView.as_view()),
    path('home/posts/', views.GetHomePostsView.as_view()),
    path('handle_following/', views.HandleFollowingView.as_view()),
    path('search_profile/<str:search>/', views.SearchProfileView.as_view()),
    path('activate_users/', views.ActivateUsersView.as_view()),
    path('toggle_post_like/', views.TogglePostLikeView.as_view()),
    path('get_post_comments/', views.GetPostCommentsView.as_view()),
    path('add_post_comments/', views.AddPostCommentsView.as_view()),
    path('get_post_comment_replies/', views.GetPostCommentRepliesView.as_view()),
]
