from django.shortcuts import render


def index(request):
    # study the request
    return render(request, 'taskmodule/index.html') # rendering the template
