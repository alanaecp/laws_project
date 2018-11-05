from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='members'),
    path('<int:member_id>', views.member, name='member'),
]
