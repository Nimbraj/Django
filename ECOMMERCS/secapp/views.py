from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def Greet(request):
    st = '<h1>Good morning, welcome to Django class!</h1>'
    return HttpResponse(st)

def time(request):
    # Correct method: datetime.datetime.now() instead of datetime.datetime.new()
    tt = datetime.datetime.now()
    msg = "Current server date and time: " + str(tt)
    # Correct function name: HttpResponse (capital H and R)
    return HttpResponse(msg)
