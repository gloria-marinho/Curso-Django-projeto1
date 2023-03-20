from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/pages/home.html', context={
        'name':'gloria',
    })

def contato(request):
    return HttpResponse('contato')
    return render(request, 'me-apague/temp.html')


def sobre(request):
    return HttpResponse('sobre')
