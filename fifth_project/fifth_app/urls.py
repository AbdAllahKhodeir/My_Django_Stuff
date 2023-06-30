from django.urls import path
from fifth_app import views

urlpatterns = [
    path('', views.users, name='users'),
]