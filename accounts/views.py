from django.shortcuts import render, redirect
from django.http import HttpResponse
from travelers.models import Traveler
from django.contrib.auth.models import User, auth
from travelers.models import TravelersPost
from django.contrib import messages
from django.template import RequestContext


def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        user_type = request.POST["user_type"]

        new_user = Traveler.objects.create(
            username=username,
            email=email,
            phone=phone,
            password=password,
            user_type=user_type,
        )
        new_user.save()
        return redirect("post_requests")
    else:
        return render(request, "signUp.html")


def sign_in(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user_details = Traveler.objects.get(email=email, password=password)
            request.session["email"] = user_details.email
            return redirect("post_requests")
        except Traveler.DoesNotExist as e:
            return redirect("sign_in")
    else:
        return render(request, "signIn.html")
