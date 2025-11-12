import logging
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.conf import settings
from requests_oauthlib import OAuth2Session
from django.contrib.auth import get_user_model
from djoser.conf import settings as djoser_settings
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from djoser import utils
from djoser.serializers import TokenSerializer, PasswordResetConfirmSerializer
from rest_framework.generics import GenericAPIView
from urllib.parse import urlencode
from authAPI.serializers import TokenCreateSerializer

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

    web_url = settings.POST_ACTIVATE_REDIRECT_URL + 'api/auth/users/activation/'  # URL comes from Djoser library
    return render(request, 'activate_user.html',
                  {'uid': uid,
                   'token': token,
                   'activation_url': web_url,
                   'redirect_url': settings.POST_ACTIVATE_REDIRECT_URL
                   })


def pwd_reset(request, uid, token):
    """
    Used to reset password,
    sends POST request to /api/auth/users/reset_password_confirm/ route
    internally to reset user password.
    Link to this route is sent via email to user for verification
    """

    web_url = settings.POST_ACTIVATE_REDIRECT_URL + 'api/auth/users/reset_password_confirm/'  # Djoser endpoint
    return render(request, 'reset_password.html',
                  {
                      'uid': uid,
                      'token': token,
                      'reset_url': web_url,
                      'redirect_url': settings.POST_ACTIVATE_REDIRECT_URL
                  })


def get_social_user(email, request, callback, service):
    if not email:
        logger.error(f'Email not found for {service} user')
        return HttpResponseNotFound('<h1>Email not found</h1>')

    user, created = get_user_model().objects.get_or_create(email=email)
    if created:
        user.username = email
        user.save()
    if not user.is_active:
        user.is_active = True
        user.save()
    token, created = Token.objects.get_or_create(user=user)

    web_url = settings.POST_ACTIVATE_REDIRECT_URL + '#/dashboard'

    return render(request, callback,
                  {'token': token,
                   'url': web_url
                   })


def GoogleOAuth2(request):
    error = request.GET.get('error', None)
    if error is not None and error != '':
        error = error.strip().replace('\x00', '').replace('\r', '').replace('\n', '')[:200]
        logger.error(f'Google OAuth2 error: {error}')
        query = urlencode({'error': error})
        return redirect(f'{settings.POST_ACTIVATE_REDIRECT_URL}#/login?{query}')

    state = request.GET.get('state', None)
    code = request.GET.get('code', None)

    if state is None or state == '' or code is None or code == '':
        return HttpResponseNotFound('<h1>Page Not Found</h1>')

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

    return get_social_user(user_info['email'], request, 'google_callback.html', 'google')


def GitHubOAuth2(request):
    error = request.GET.get('error', None)
    if error is not None and error != '':
        error = error.strip().replace('\x00', '').replace('\r', '').replace('\n', '')[:200]
        logger.error(f'GitHub OAuth2 error: {error}')
        query = urlencode({'error': error})
        return redirect(f'{settings.POST_ACTIVATE_REDIRECT_URL}#/login?{query}')

    state = request.GET.get('state', None)
    code = request.GET.get('code', None)

    if state is None or state == '' or code is None or code == '':
        return HttpResponseNotFound('<h1>Page Not Found</h1>')

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
        logger.error(f'Failed to fetch token from GitHub: {e}')
        return HttpResponseNotFound('<h1>Failed to authenticate with GitHub</h1>')

    try:
        user_info = github.get('https://api.github.com/user').json()
    except Exception as e:
        logger.error(f'Failed to get user info from GitHub: {e}')
        return HttpResponseNotFound('<h1>Failed to get user info from GitHub</h1>')

    primary_email = f"{user_info['id']}+{user_info['login']}@users.noreply.github.com"

    return get_social_user(primary_email, request, 'github_callback.html', 'github')


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
            'auth_token': token_serializer_class(token).data['auth_token'],
            'user_id': serializer.user.id
        }
        return Response(data=data, status=status.HTTP_200_OK)


class CustomPasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        if not user.is_active:
            user.is_active = True
            user.save()

        serializer.save()  # This sets the new password

        return Response(status=status.HTTP_204_NO_CONTENT)
