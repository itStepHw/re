from django.shortcuts import render
from django.http import HttpResponse

from .models import tempModel

# Create your views here.


def index(request):
    temp = tempModel.objects.extra(where=["age % 2 = 0"])
    cntx = {
        'temps': temp,
    }

    return render(request, 'regular_ex/index.html', cntx)


def about(request):
    return HttpResponse('about')


def contacts(request):
    return HttpResponse('contacts')