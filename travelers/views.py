from django.shortcuts import render
from django.http import HttpResponse


def land_page(request):
    return render(request, "index.html")


def post_request(request):
    return render(request, "flightDetails.html")


def sign_up(request):
    return render(request, "travelerSign.html")
