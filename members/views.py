from django.shortcuts import render

from .models import Member

def index(request):
    
    #members = Member.objects.all()
    professores = Member.objects.all().filter(is_professor=True)
    mestrandos = Member.objects.all().filter(is_master=True)
    graduandos = Member.objects.all().filter(is_undergraduate=True)
    

    context = {
        "professores": professores,
        "mestrandos": mestrandos,
        "graduandos": graduandos
    }
    return render(request, 'members/index.html',context)

def member(request, member_id):
    return render(request, 'members/member.html')