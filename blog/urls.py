from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    path('category/<str:name>/', views.category_detail, name='category-detail'),
    path('delete/comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete/post/<int:post_id>/', views.delete_post, name='delete_post'),
]
