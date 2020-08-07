from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.post_list, name='post_list'),
    # localhost:8000/post/{id}
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # localhost:8000/post/new
    path('post/new/', views.post_new, name='post_new'),
    # localhost:8000/post/{id}/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # localhost:8000/post/{id}/remove
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    # localhost:8000/post/{id}/comment
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # localhost:8000/comment/{id}/approve
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    # localhost:8000/comment/{id}/remove
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove')
]
