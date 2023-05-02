from django.urls import path

from . import views

urlpatterns = [
    path('register/, views.regoster_view, name='register'),
]
