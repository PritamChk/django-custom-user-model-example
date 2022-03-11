from django.shortcuts import render
from django.http.request import HttpRequest

def test(request):
    return HttpRequest("hello")
