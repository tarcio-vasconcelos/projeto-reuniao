from allauth.socialaccount.models import SocialAccount

def get_foto_google(user):
# 1. Garante que o usuário existe e está autenticado
    if not user or not user.is_authenticated:
        return None

    # 2. Usa .filter().first() para evitar DoNotExist e MultipleObjectsReturned
    social_account = SocialAccount.objects.filter(user=user, provider='google').first()
    
    if not social_account:
        return None

    # 3. Garante que extra_data é um dicionário antes de chamar .get()
    extra_data = social_account.extra_data or {}
    return extra_data.get('picture')