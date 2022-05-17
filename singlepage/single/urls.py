from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name = 'index'),
    path('sections/<int:page>', views.section, name = 'section')
]