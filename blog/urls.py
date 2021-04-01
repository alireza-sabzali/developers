from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.post_detail, name='post-detail'),
    path('category/<str:name>/', views.category_detail, name='category-detail'),
    path('comments/<int:pk>', views.comments_create, name='comments_create'),
    path('search/', views.post_search, name='post_search'),
]
