from django.shortcuts import render
from .forms import Registration

def fist_views(request):
    submit = False
    name = ""

    if request.method == 'POST':
        form = Registration(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            marks = form.cleaned_data.get('marks')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            cpassword = form.cleaned_data.get('cpassword')
            feedback = form.cleaned_data.get('feedback')

            print(name, age, marks, feedback, age, email)

            submit = True
            form = Registration()   # ⭐ reset the form after successful submission

    else:
        form = Registration()

    return render(request, 'testapp/index.html', {
        'data': form,
        'name': name,
        'submit': submit
    })
