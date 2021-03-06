from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register),
    path('token/', views.token),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
    path('hello_world/', views.hello_world),
    path('authorization_code/', views.authorization_code),
    
]
