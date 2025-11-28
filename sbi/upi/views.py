from django.shortcuts import render
from django.http import HttpRespones
def upiviews(request):
    st = '<h1> the function is bal</h1>'
    return HttpResponse(st)

