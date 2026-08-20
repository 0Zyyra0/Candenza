from django.urls import path
from .views import index_view, load_more_posts, post_detail

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('blog/load-more/', load_more_posts, name='load_more_posts'),
    path('blog/<int:pid>/', post_detail, name='post_detail'),
    path('blog/load-more/',load_more_posts,name='load_more_posts'),
]