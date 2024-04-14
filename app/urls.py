from django.urls import path

from .views import *

app_name = 'app'
urlpatterns = [
    path("app/", index, name="index"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:pk>/", detail, name="detail"),
    path("<int:pk>/vote/", vote, name="vote"),
]