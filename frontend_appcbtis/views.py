from django.shortcuts import render
from . models import Alumno

# Create your views here.
def index(request):
    """
    Render the index page of the application.
    """
    return render(request, 'frontend_appcbtis/index.html',{"alumnos": Alumno.objects.all()})
