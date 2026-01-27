from django.urls import path
from . import views, apis

urlpatterns = [
    path('', views.home_page, name = 'home-page'),
    path('about/', views.about_page, name = 'about-page'),
    path('posts/', views.all_posts, name = 'all-posts'),
    path('posts/create/', views.create_post, name = 'create-post'),

    # 
    path('api/posts/', apis.all_posts)
]