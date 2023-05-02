from django.shortcuts import render


def register_vienw(request):
    return render(request, 'authors/pages/register_view.html')

