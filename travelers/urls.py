from django.urls import path
from . import views

urlpatterns = [
    path('post-request/', views.post_request),
]