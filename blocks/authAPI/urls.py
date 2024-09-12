from django.urls import re_path
from authAPI import views as authAPI_views


urlpatterns = [
    # GitHub OAuth2 callback
    re_path(r'^github-callback', authAPI_views.GitHubOAuth2, name='github-callback'),
    re_path(r'^google-callback', authAPI_views.GoogleOAuth2),
    re_path(r'^users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$',
            authAPI_views.activate_user),
    re_path(r'user/token/', authAPI_views.CustomTokenCreateView.as_view())
]
