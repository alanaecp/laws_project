from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='publications'),
    path('<int:publication_id>', views.publication, name='publication'),
]
