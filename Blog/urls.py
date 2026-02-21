from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('detail/<str:title>', views.article_detail , name='article_detail'),
]
