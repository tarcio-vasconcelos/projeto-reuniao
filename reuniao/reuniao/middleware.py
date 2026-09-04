# seu_app/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class ExigirLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Rotas que devem ficar acessíveis mesmo sem login
        rotas_liberadas = [
            '/accounts/login/',
            '/accounts/logout/',
            '/accounts/google/login/',
            '/accounts/google/login/callback/',
            '/admin/login/',
        ]

        # Libera arquivos estáticos e admin (opcional, ajuste como quiser)
        caminhos_liberados = ['/static/', '/media/']

        path = request.path

        precisa_bloquear = (
            not request.user.is_authenticated
            and path not in rotas_liberadas
            and not any(path.startswith(p) for p in caminhos_liberados)
        )

        if precisa_bloquear:
            return redirect('account_login')

        return self.get_response(request)