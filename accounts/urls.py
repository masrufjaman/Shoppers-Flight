from django.urls import path
from accounts.views import sign_up, sign_in


path("sign-up/", sign_up, name="sign_up"),
path("sign-in/", sign_in, name="sign_in"),
