from django.shortcuts import render, get_object_or_404
from .utils import get_foto_google
from .models import Usuarios
from django.contrib.auth.models import User

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
    if request.method == "POST":
        nome = request.POST.get("usuario")
        mail = request.POST.get("mail")
        area = request.POST.get("area")
        setor = request.POST.get("cargo")
        local = request.POST.get("local")
        peso = request.POST.get("peso")

        if User.objects.filter(username=nome).exists() or User.objects.filter(email=mail).exists():
            contexto["erro"] = "O usuário duplicado!"
            return render(request, "users/users.html", contexto)

        User.objects.create(
            username=nome,
            email=mail
        )

        usuario = Usuarios.objects.order_by('-id').first()
        usuario.area = area
        usuario.setor = setor
        usuario.local = local
        usuario.peso = peso
        usuario.save()
    return render(request, "users/users.html", contexto)