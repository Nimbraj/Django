def index_views(request):
    if request.method == 'POST':
        form = MoviesedForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("FORM ERRORS:", form.errors)   # <-- CHECK ERRORS
    else:
        form = MoviesedForm()

    return render(request, 'testapp/index.html', {'form': form})
