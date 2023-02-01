from django.urls import path

from project_app import views

urlpatterns =[
    path('', views.project_app, name='project_app')
]