"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, ofertas, register, salir, publicaciones, tematicas



urlpatterns = [
    path('', home, name='home'),
    path('ofertas/', ofertas, name='ofertas'),
    path('register/', register, name='register'),
    path('logout/', salir, name='salir'),  # Ruta para logout
    path('', home, name='home'),
    path('publicaciones/', publicaciones, name='publicaciones'),  # Publicaciones
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('tematicas/', tematicas, name='tematicas'),
]