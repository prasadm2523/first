from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def application(request):
    return HttpResponse('How r u')
