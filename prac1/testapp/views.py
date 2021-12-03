from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s='<h1>demo for practicing github</h1>'
    return HttpResponse(s)
