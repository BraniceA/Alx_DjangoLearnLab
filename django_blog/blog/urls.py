from django.urls import path
from .views import home, posts, TaggedPostListView  # Import the views named home, posts, and TaggedPostListView
# from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .views import *   # Custom registration view

urlpatterns = [
    path('', home, name='home'),  # This makes http://127.0.0.1:8000/ show your HTML file
    path('posts/', posts, name='posts'),  # Add this line
 # Authentication views
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Custom registration view
    path('register/', register, name='register'),
    path('profile/', auth_views.LoginView.as_view(template_name='blog/profile.html'), name='profile'),  # Profile page after login
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', EditCommentView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete-comment'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('tags/<str:tag>/', TaggedPostListView.as_view(), name='posts_by_tag'),
    ]

