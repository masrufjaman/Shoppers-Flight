from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account-info', views.account_info, name='account_info'),
    path('my-requests', views.my_requests, name='my_requests'),
    path('post-request/', views.post_request, name='post-request'),
    path('flight-details', views.flight_details, name='flight_details'),
    path('complaints', views.complaints, name='complaints'),
    path('payments-&-refunds', views.payments_and_refunds, name='payments_and_refunds'),
    path('shipping-address', views.shipping_address, name='shipping_address'),
    path('track-request', views.track_request, name='track_request'),
    path('pricing', views.pricing, name='pricing'),
    path('support-tickets', views.support_tickets, name='support_tickets'),
    
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login, name='login'),
]
