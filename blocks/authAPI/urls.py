from django.conf.urls import url
from authAPI import views as authAPI_views


urlpatterns = [

    # GitHub OAuth2 callback
    url(r'^github-callback', authAPI_views.GitHubOAuth2, name='github-callback'),
    
    url(r'^google-callback', authAPI_views.GoogleOAuth2),
    url(r'^users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$',
        authAPI_views.activate_user),
    url(r'user/token/', authAPI_views.CustomTokenCreateView.as_view())
]
