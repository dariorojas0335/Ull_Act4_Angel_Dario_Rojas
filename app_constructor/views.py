from django.shortcuts import render

# Create your views here.
def inicio(request):
    arquitectos = [
        {"nombre": "Ana García", "especialidad": "Residencial", "proyectos": 15},
        {"nombre": "Luis Pérez", "especialidad": "Comercial", "proyectos": 10},
        {"nombre": "Marta Rodríguez", "especialidad": "Diseño de Interiores", "proyectos": 20},
    ]
    context = {
        'arquitectos': arquitectos
    }
    return render(request, 'index.html', context)