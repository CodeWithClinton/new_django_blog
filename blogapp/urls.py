from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("article/<slug:slug>", views.detail, name="detail"),
    path("like_blog", views.like_blog, name = "like"),
    path("add_comment", views.addComment, name = "add_comment")
]
