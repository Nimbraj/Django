from django.shortcuts import render
from .forms import Registration
from .models import Student # import the model

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
            feedback = form.cleaned_data.get('feedback')

            # Save to database
            Student.objects.create(
                name=name,
                email=email,
                age=age,
                marks=marks,
                password=password,
                feedback=feedback
            )

            submit = True
            form = Registration()  # reset form after submission

    else:
        form = Registration()

    return render(request, 'testapp/index.html', {
        'data': form,
        'name': name,
        'submit': submit
    })
