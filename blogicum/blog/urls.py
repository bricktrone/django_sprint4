"""import."""
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostsListView.as_view(), name='index'),
    path('posts/<int:post>/', views.PostDetailView.as_view(),
         name='post_detail'),
    path('posts/<int:post>/comment/', views.CreateCommentView.as_view(),
         name='add_comment'),
    path('posts/<int:post>/edit_comment/<int:comment>/',
         views.UpdateCommentView.as_view(),
         name='edit_comment'),
    path('posts/<int:post>/delete_comment/<int:comment>/',
         views.DeleteCommentView.as_view(),
         name='delete_comment'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(),
         name='category_posts'),
    path('posts/create/', views.CreatePostView.as_view(), name='create_post'),
    path('posts/<int:post>/edit/', views.UpdatePostView.as_view(),
         name='edit_post'),
    path('posts/<int:post>/delete/', views.DeletePostView.as_view(),
         name='delete_post'),
    path('profile/edit/', views.UpdateUserView.as_view(),
         name='edit_profile'),
    path('profile/<str:username>/', views.UserDetailView.as_view(),
         name='profile')
]
