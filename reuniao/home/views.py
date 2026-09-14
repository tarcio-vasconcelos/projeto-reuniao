from django.shortcuts import render
from .utils import get_foto_google
from .models import Usuarios

# Create your views here.
def home(request):
    foto = get_foto_google(request.user)
    return render(request,"home/index.html",{
        'usuario': request.user,
        'foto': foto
})

def sugestoes(request):
    foto = get_foto_google(request.user)
    return render(request,"sugestoes/sugestoes.html",{
        'usuario': request.user,
        'foto': foto
})

def users(request):
    foto = get_foto_google(request.user)
    usuarios = Usuarios.objects.all()
    contexto = {
        'usuarios': usuarios,
        'usuario': request.user,
        'foto': foto,
    }
    return render(request, "users/users.html", contexto)