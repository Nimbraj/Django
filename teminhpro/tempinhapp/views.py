from django.shortcuts import render

def base_view(request):
    return render(request, 'testapp/Base.html')

def first_view(request):
    return render(request, 'testapp/first.html')


def second_view(request):
    return render(request, 'testapp/second.html')



def thread_view(request):
    return render(request, 'testapp/thread.html')


