from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def post_list(request):
    return HttpResponse("Hello World from Django!")
