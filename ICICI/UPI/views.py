from django.shortcuts import render
from django.http import HttpResponse  # ✅ Correct import (case-sensitive)

# Create your views here.
def BHIM(request):
    return HttpResponse("<h1>The BHIM methods</h1>")

def phonepe(request):
    return HttpResponse("<h1>The PhonePe methods</h1>")
