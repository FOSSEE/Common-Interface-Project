from django.urls import re_path
from authAPI import views as authAPI_views
from .views import CustomPasswordResetConfirmView


urlpatterns = [
    # GitHub OAuth2 callback
    re_path(r'^github-callback', authAPI_views.GitHubOAuth2, name='github-callback'),
    re_path(r'^google-callback', authAPI_views.GoogleOAuth2),
    re_path(r'^users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$',
            authAPI_views.activate_user),
    re_path(r'user/token/', authAPI_views.CustomTokenCreateView.as_view()),
    re_path(r'^users/reset/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$',
            authAPI_views.pwd_reset),
    re_path(r'^auth/users/reset_password_confirm/?$', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm')
]
