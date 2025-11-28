from django.shortcuts import render
from.models import Employee
def exctacting(request):
    data=Employee.object.all()
    return render(request,'testapp/index.html',{'data':data})
    
# Create your views here.
