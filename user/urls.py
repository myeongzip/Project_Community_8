from django.urls import path

from user import views


urlpatterns = [
    path('index/', views.index),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path("signout/", views.signout),
]