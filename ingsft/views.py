from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render, redirect
from apps.inscripcion.forms import horarioForm, loginForm
from django.contrib.auth.decorators import login_required
from apps.director.models import Director, Estudiante, Students


@login_required()
def horario(request):
    if request.method == 'POST':
        form = horarioForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('goEnviado')
    else:
        form = horarioForm()
    return render(request, 'home.html/', {'form': form})



def Inicio(request):
    if request.method == 'POST':
        usuario = request.POST["username"]

        director = Director.objects.filter(username=usuario)
        if director:
            for d in director:
                if request.POST["password"] == d.password:
                    return render(request, 'dashboard.html', {'director': d})

        estudiant = Students.objects.filter(username=usuario)
        if estudiant:
            for e in estudiant:
                if request.POST["password"] == e.password:
                    return render(request, 'home.html', {'estudiante': e})






    return render(request, 'index.html')

def Enviado(request):
    return render(request,'enviado.html/')

def homeDirector(request):
    return render(request, 'dashboard.html')

def Convocatoria(request):
    return render(request, 'Convocatoria.html')

def Estudiante1(request):
    return render(request, 'estudiantes.html')

def Proveedor(request):
    return render(request, 'proveedores.html')

def Asistente(request):
    return render(request, 'asistentes.html')

def DueñosCafeteria(request):
    return render(request, 'dueñosdecafeteria.html')


