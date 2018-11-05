from django.shortcuts import render
from .models import Project

def index(request):
    projetos = Project.objects.all()    

    context = {
        "projetos": projetos
    }
    return render(request, 'projects/index.html', context)


def project(request, listing_id):
    return render(request, 'projects/project.html')