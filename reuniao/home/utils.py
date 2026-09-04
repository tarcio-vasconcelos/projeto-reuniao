from allauth.socialaccount.models import SocialAccount

def get_foto_google(user):
    try:
        social_account = SocialAccount.objects.get(user=user, provider='google')
        return social_account.extra_data.get('picture')
    except SocialAccount.DoesNotExist:
        return None