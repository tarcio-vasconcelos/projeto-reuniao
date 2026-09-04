from django.shortcuts import render
from .utils import get_foto_google

# Create your views here.
def home(request):
    foto = get_foto_google(request.user)
    return render(request,"home/index.html",{
        'usuario': request.user,
        'foto': foto
})