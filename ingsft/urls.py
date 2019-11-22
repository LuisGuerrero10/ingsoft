"""ingsft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ingsft.views import horario, Enviado, Inicio, homeDirector, Convocatoria, Estudiante1, Proveedor, Asistente, DueñosCafeteria
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horario/', horario, name='goHorario'),
    path('login/', LoginView.as_view(), name="login_url"),
    path('enviado/', Enviado, name='goEnviado'),
    path('inicio/', Inicio, name='goInicio'),
    path('director/', homeDirector, name='goHome'),
    path('inicio/dashboard', homeDirector, name='goHome'),
    path('inicio/Convocatoria', Convocatoria, name='goConvocatoria'),
    path('inicio/estudiantes', Estudiante1, name='goEstudiante'),
    path('inicio/proveedores', Proveedor, name='goproveedores'),
    path('inicio/dueñosdecafeteria', DueñosCafeteria, name='godueñoscafeteria'),
    path('inicio/asistentes', Asistente, name='goasistentes'),
]

