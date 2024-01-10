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
    path('add_post_comment/', views.AddPostCommentView.as_view()),
    path('get_post_comment_replies/', views.GetPostCommentRepliesView.as_view()),
    path('add_post_comment_reply/', views.AddPostCommentReplyView.as_view()),
    path('toggle_comment_like/', views.ToggleCommentLikeView.as_view()),
    path('toggle_comment_dislike/', views.ToggleCommentDislikeView.as_view()),
    path('toggle_reply_like/', views.ToggleReplyLikeView.as_view()),
    path('toggle_reply_dislike/', views.ToggleReplyDislikeView.as_view()),
    path('edit_profile/', views.EditProfileView.as_view()),
    path('profile/<str:username>/', views.GetProfileView.as_view()),
    path('profile_posts/<str:profile_id>/', views.ProfilePostsView.as_view()),
    path('delete_profile_posts/', views.DeletePostView.as_view()),
    path('delete_account/', views.DeleteAccountView.as_view()),
]
