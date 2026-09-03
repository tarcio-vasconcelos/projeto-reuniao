from allauth.socialaccount.signals import pre_social_login
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.dispatch import receiver

@receiver(pre_social_login)
def antes_login_social(sender, request, sociallogin, **kwargs):
    if sociallogin.is_existing:
        print(f'Usuário JÁ EXISTIA: {sociallogin.user.email}')
    else:
        messages.error(request, "Usuário inexistente! Por favor entre em contato com o Administrador!")
        raise ImmediateHttpResponse(redirect('login'))