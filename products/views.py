from django.http import HttpResponse
from django.shortcuts import render


# products, call index function
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New Products')

