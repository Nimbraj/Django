from django.shortcuts import render
def index_view(request):
    return render(request,'testapp/Home.html')

def sports_view(request):
    return render(request,'testapp/sports.html')
def politics_view(request):
    return render(request,'testapp/politics.html')
def movies_view(request):
    return render(request,'testapp/movies.html')
# Create your views here.
