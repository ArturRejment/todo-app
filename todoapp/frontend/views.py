from django.shortcuts import render

# Create your views here.


def list(response):
    context = {}
    return render(response, 'frontend/list.html', context)
