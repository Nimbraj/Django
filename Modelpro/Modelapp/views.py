from django.shortcuts import render
from Modelapp.models import Student

def extraction(request):
    st_data = Student.objects.all()
    return render(request, 'testapp/index.html', {'st_data': st_data})
