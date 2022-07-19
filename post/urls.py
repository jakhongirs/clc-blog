from django.urls import path
from post import views

urlpatterns = [
    path('posts/', views.post_list, name="posts"),
]
