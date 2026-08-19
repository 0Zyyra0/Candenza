from django.urls import path
from .views import index_view, post_detail

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('blog/<int:pid>/', post_detail, name='post_detail'),
]