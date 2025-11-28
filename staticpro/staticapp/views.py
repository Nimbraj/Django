from django.shortcuts import render

def staticdata(request):
    my_con = {
        "name": "mayur",
        "address": "deccan Pune",
        "age": "23"
    }
    return render(request, 'testapp/index.html', my_con)
