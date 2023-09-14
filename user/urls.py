from django.urls import path

from user import views

app_name="user"

urlpatterns = [
    path('index/', views.index),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("mypage/", views.mypage, name="mypage"),
]