from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Traveler
from django.contrib.auth.models import User, auth


def land_page(request):
    return render(request, "index.html")


def post_request(request):
    return render(request, "flightDetails.html")


def sign_up(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["psw"]

        user = Traveler.objects.create(
            fullname=fullname, email=email, phone=phone,password=password
        )
        user.save()

        return redirect("post-request")
    else:
        return render(request, "travelerSign.html")


def login(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["psw"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("post-request")
        else:
            # messages.error(
            #     request, f'Invalid credentials...')
            return redirect("sign-up")
    else:
        return render(request, "login.html")
