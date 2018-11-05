from django.shortcuts import render


def index(request):
    return render(request, 'publications/index.html')


def publication(request, listing_id):
    return render(request, 'publications/publication.html')