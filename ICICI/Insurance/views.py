from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HealthIns(request):
    return HttpResponse("<h1>The claims were rejected</h1>")
