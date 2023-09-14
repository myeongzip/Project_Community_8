from django.urls import path

from user import views

app_name="user"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("mypage/", views.mypage, name="mypage"),
    path("<int:user_id>/mypage/update/", views.profile_update, name="profile_update"),
]