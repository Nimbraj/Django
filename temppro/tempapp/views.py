from django.shortcuts import render

def firstTemplate(request):

    employee = {
        "id": 101,
        "name": "Amit",
        "address": {
            "city": "Mumbai",
            "pincode": 400001
        },
        "skills": ["Java", "React", "MySQL"]
    }

    return render(request, "index.html", {"employee": employee})
