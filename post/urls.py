from django.urls import path

from post import views


urlpatterns = [
    path('post_read/', views.post_read),
    path('post_create/', views.post_create),
    path("<int:post_id>/", views.post_read_detail),
    path("<int:post_id>/delete/", views.post_delete),
    path("<int:post_id>/update/", views.post_update),
]