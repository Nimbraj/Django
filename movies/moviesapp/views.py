from django.shortcuts import render
from .forms import MoviesedForm

def index_views(request):
    if request.method == 'POST':
        form = MoviesedForm(request.POST)
        if form.is_valid():
            form.save()
            form = MoviesedForm()  # clear form after save
    else:
        form = MoviesedForm()

    return render(request, 'testapp/index.html', {'form': form})
