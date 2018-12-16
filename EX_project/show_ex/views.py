from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def demo(request):
    return HttpResponse('first_time_update_to_online_server')