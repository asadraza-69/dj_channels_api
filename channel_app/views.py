from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return JsonResponse({"Status": True})


def welcome(request):
    return render(request, 'channel_app/index.html', {})
