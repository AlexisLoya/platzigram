"""Posts urls"""
#Django
from django.urls import path
#Views
from posts import views

urlpatterns = [

    path(
        route='',
        view=views.PostFeedView.as_view(),
        name='feed'
    ),
    path(
        route='posts/new/',
        view=views.CreatePostview.as_view(),
        name='create'
    ),
    path(
        route='posts/<int:post_id>',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
]