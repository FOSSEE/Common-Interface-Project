import logging
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.conf import settings
from requests_oauthlib import OAuth2Session
from django.contrib.auth import get_user_model
from djoser.conf import settings as djoser_settings
from django.shortcuts import render
from django.http import HttpResponseNotFound
from djoser import utils
from djoser.serializers import TokenSerializer
from authAPI.serializers import TokenCreateSerializer
from blocks.settings import DOMAIN

Token = djoser_settings.TOKEN_MODEL

# Set up logging
logger = logging.getLogger(__name__)

def activate_user(request, uid, token):
    """
    Used to activate accounts,
    sends POST request to /api/auth/users/activation/ route
    internally to activate account.
    Link to this route is sent via email to user for verification
    """

    protocol = 'https://' if request.is_secure() else 'http://'
    web_url = protocol + request.get_host() + '/api/auth/users/activation/'  # noqa URL comes from Djoser library
    return render(request, 'activate_user.html',
                  {'uid': uid,
                   'token': token,
                   'activation_url': web_url,
                   'redirect_url': settings.POST_ACTIVATE_REDIRECT_URL
                   })


def GoogleOAuth2(request):
    state = request.GET.get('state', None)
    code = request.GET.get('code', None)

    if state is None or state == '' or code is None or code == '':
        return HttpResponseNotFound("<h1>Page Not Found</h1>")

    client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    client_secret = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

    google = OAuth2Session(
        client_id,
        redirect_uri=settings.GOOGLE_OAUTH_REDIRECT_URI,
        state=state
    )
    google.fetch_token(
        'https://accounts.google.com/o/oauth2/token',
        client_secret=client_secret,
        code=code
    )

    user_info = google.get(
        'https://www.googleapis.com/oauth2/v1/userinfo').json()

    if user_info['email']:
        user, created = get_user_model().objects.get_or_create(
            email=user_info['email'])
        if created:
            user.username = user_info['email']
            user.save()
        if not user.is_active:
            user.is_active = True
            user.save()
        token, created = Token.objects.get_or_create(user=user)

        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + DOMAIN + '/#/dashboard'

        return render(request, 'google_callback.html',
                      {
                          "token": token,
                          "url": web_url
                      })


def GitHubOAuth2(request):
    state = request.GET.get('state', None)
    code = request.GET.get('code', None)

    if state is None or state == '' or code is None or code == '':
        return HttpResponseNotFound("<h1>Page Not Found</h1>")

    client_id = settings.SOCIAL_AUTH_GITHUB_KEY
    client_secret = settings.SOCIAL_AUTH_GITHUB_SECRET

    github = OAuth2Session(
        client_id,
        redirect_uri=settings.GITHUB_OAUTH_REDIRECT_URI,
        state=state
    )
    try:
        github.fetch_token(
            'https://github.com/login/oauth/access_token',
            client_secret=client_secret,
            code=code
        )
    except Exception as e:
        logger.error(f"Failed to fetch token from GitHub: {e}")
        return HttpResponseNotFound("<h1>Failed to authenticate with GitHub</h1>")

    try:
        user_info = github.get('https://api.github.com/user').json()
    except Exception as e:
        logger.error(f"Failed to get user info from GitHub: {e}")
        return HttpResponseNotFound("<h1>Failed to get user info from GitHub</h1>")

    primary_email = f"{user_info['id']}+{user_info['login']}@users.noreply.github.com"

    if primary_email:
        user, created = get_user_model().objects.get_or_create(email=primary_email)
        if created:
            user.username = primary_email
            user.save()
        if not user.is_active:
            user.is_active = True
            user.save()
        token, created = Token.objects.get_or_create(user=user)

        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + DOMAIN + '/#/dashboard'

        return render(request, 'github_callback.html', {
            "token": token.key,
            "url": web_url
        })
    else:
        logger.error("Primary email not found for GitHub user")
        return HttpResponseNotFound("<h1>Email not found</h1>")


class CustomTokenCreateView(utils.ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to obtain user authentication token.
    """

    serializer_class = TokenCreateSerializer
    permission_classes = [permissions.AllowAny]

    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = TokenSerializer
        data = {
            'auth_token': token_serializer_class(token).data["auth_token"],
            'user_id': serializer.user.id
        }
        return Response(data=data, status=status.HTTP_200_OK)
