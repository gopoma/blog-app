from django.urls import path

# from .views import home, posts, recent_posts, post, create_post, edit_post, delete_post

from . import views
app_name = "posts"
urlpatterns = [
    path('', views.posts, name='posts_list'),
    path('recent-posts/', views.recent_posts, name="posts_recent"),
    path('create', views.create_post, name="post_create"),
    path('<int:id>', views.post, name="post_detail"),
    path('edit/<int:id>', views.edit_post, name="post_edit"),
    # path('posts/edit/<int:id>/<str:year>', views.edit_post)
    path('delete/<int:id>', views.delete_post, name="post_delete")
]