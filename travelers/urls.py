from django.urls import path
from . import views

urlpatterns = [
    path('', views.land_page, name='land-page'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login, name='login'),
    path('post-request/', views.post_request, name='post-request'),
]