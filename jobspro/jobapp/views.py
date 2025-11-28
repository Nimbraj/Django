from django.shortcuts import render
from .models import Punejob, Bangjob, Bhiharjob

def job_home(request):
    pune_jobs = Punejob.objects.all()
    bang_jobs = Bangjob.objects.all()
    bihar_jobs = Bhiharjob.objects.all()

    context = {
        'pune_jobs': pune_jobs,
        'bang_jobs': bang_jobs,
        'bihar_jobs': bihar_jobs,
    }
    return render(request, 'index.html', context)
