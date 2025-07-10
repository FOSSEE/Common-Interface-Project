from djoser import email
from django.conf import settings


class CustomActivationEmail(email.ActivationEmail):
    def get_context_data(self):
        context = super().get_context_data()
        context['protocol'] = settings.DEFAULT_PROTOCOL
        return context


class CustomPasswordResetEmail(email.PasswordResetEmail):
    def get_context_data(self):
        context = super().get_context_data()
        context['protocol'] = settings.DEFAULT_PROTOCOL
        return context
