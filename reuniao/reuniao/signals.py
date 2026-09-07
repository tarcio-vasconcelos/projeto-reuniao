from allauth.socialaccount.signals import pre_social_login
from allauth.core.exceptions import ImmediateHttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.dispatch import receiver
from django.contrib.auth import logout


@receiver(pre_social_login)
def antes_login_social(sender, request, sociallogin, **kwargs):
    # Se já existe um SocialAccount vinculado, não faz nada, segue o fluxo normal
    if sociallogin.is_existing:
        return

    email = sociallogin.user.email

    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        messages.error(request, 'Usuário inexistente! Por favor entre em contato com o Administrador!')
        raise ImmediateHttpResponse(redirect('login'))
    else:
        # Conecta a conta do Google ao usuário já existente no banco
        sociallogin.connect(request, user)