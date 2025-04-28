from django.contrib import admin
from django.urls import path
from publicpostsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', views.posts),
    path('api/like_post/<int:post_id>/', views.like_post),
]