from django.urls import path

<<<<<<< HEAD

from post import views

app_name = "post"


urlpatterns = [
    path('', views.post_read, name="post_list"), # 지우님 설정 url post_read/ -> root.html과 연결된
    path('create/', views.post_create, name="create"),
    path("<int:post_id>/", views.post_read_detail, name="post_detail"),
    path("<int:post_id>/delete/", views.post_delete, name ="delete"),
    path("<int:post_id>/update/", views.post_update, name="update"),
=======
from post import views


urlpatterns = [
    path('post_read/', views.post_read),
    path('post_create/', views.post_create),
    path("<int:post_id>/", views.post_read_detail),
    path("<int:post_id>/delete/", views.post_delete),
    path("<int:post_id>/update/", views.post_update),
>>>>>>> 926a635289a811d5d5e8d55740c53b193b89c6e8
]