from django.shortcuts import render

def index(request):
    return render(request, 'areas/index.html')

def details(request,area_id):
    return render(request, 'areas/details.html')