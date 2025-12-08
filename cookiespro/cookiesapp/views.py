from django.shortcuts import render

def cookies_count(request):
    count = int(request.COOKIES.get('count', 0))
    count += 1

    response = render(request, 'testapp/index.html', {'count': count})
    response.set_cookie('count', count)

    return response
