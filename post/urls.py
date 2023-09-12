from django.urls import path

from post import views


urlpatterns = [
    path('post_read/', views.post_read),
    path('post_create/', views.post_create),
    path('create/', views.create),
  
]