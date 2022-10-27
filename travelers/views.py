from django.shortcuts import render
from django.http import HttpResponse

def post_request(request):
    return render(request, 'index.html')