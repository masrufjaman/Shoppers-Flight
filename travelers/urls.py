from django.urls import path
from . import views

urlpatterns = [
    path('', views.land_page, name='land-page'),
    path('post-request/', views.post_request, name='post-request'),
]