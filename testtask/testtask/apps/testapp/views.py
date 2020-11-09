from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from . import management as mn
from . import reports as rep
import random


# Create your views here.
def index(request):

    a = mn.management(request)
    context = {'list': a}

    return render(request, 'index/index.html', context)

def report(request):

    a = rep.report(request)
    context = {'list': a}

    return render(request, 'index/report.html', context)