from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('sugestoes', views.sugestoes, name='sugestoes'),
    path('users', views.users, name='usuarios')
]
