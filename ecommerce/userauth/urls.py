from django.urls import path
from userauth import views


urlpatterns = [
    path('sign-up/', views.signup, name ='sign-up')
]