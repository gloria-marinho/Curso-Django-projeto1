from django.urls import path

from . import views

app_name = 'authors'

urlpatterns = [
    path('register/, views.regoster_view, name='register'),
    path('register/create/', views.register_create, name='create'),   
]
