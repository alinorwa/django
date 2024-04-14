from django.urls import path

from .views import *

app_name = 'blog'
urlpatterns = [
    path("", all_posts, name="all_posts"),
    path("detail/<int:pk>/", detail, name="detail"),
   
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
]