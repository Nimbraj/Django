from django.shortcuts import render
from django.http import HttpRespones
def insu(request):
    st = '<h1> the function is insu</h1>'
    return HttpResponse(st)

