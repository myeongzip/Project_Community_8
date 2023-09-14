from django.urls import path


from post import views

app_name = "post"


urlpatterns = [
    path('', views.post_read, name="post_list"), # 지우님 설정 url post_read/ -> root.html과 연결된
    path('create/', views.post_create, name="create"),
    path("<int:post_id>/", views.post_read_detail, name="post_detail"),
    path("<int:post_id>/delete/", views.post_delete, name ="delete"),
    path("<int:post_id>/update/", views.post_update, name="update"),
]

