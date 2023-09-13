from django.urls import path

from user import views


urlpatterns = [
    path('index/', views.index),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
<<<<<<< HEAD
    path("mypage/", views.mypage, name="mypage"),
=======
>>>>>>> 926a635289a811d5d5e8d55740c53b193b89c6e8
]