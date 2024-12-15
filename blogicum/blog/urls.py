from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category'
    ),
    path('', views.index, name='post_index'),
    path(
        'posts/<int:id>/',
        views.post_detail,
        name='post_detail'),
]
