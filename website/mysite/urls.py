from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mysite-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='mysite-about'),
    path('comments/<int:pk>/', views.comments, name='comments'),
]
