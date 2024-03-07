from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homeView, name="home"),
    path('login', loginView, name="login"),
    path('logout', logoutView, name="logout"),
    path('cadastro', cadastroView, name="cadastro"),
    path('app', goToAppView, name="GoToApp"),
    path('vips', vipsView, name="vips"),
    path('cadastrosClientes', cadClientesView, name="cadastroClientes"),
    
    
    
    
    
    # path('api', include(router.urls) ),
]
