from django.shortcuts import render
from areas.models import Area

def index(request):
    areas = Area.objects.all()    
    context = {
        'showcase':True,
        'areas': areas
    }
    return render(request, 'pages/index.html', context)

 