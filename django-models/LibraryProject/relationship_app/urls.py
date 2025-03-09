from django.urls import path
from .Admin import admin_dashboard
from .Librarian import librarian_dashboard
from .Member import member_dashboard
from . import views  # Import views from the current module
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),  
     path('admin/', admin_dashboard, name='admin_dashboard'),
    path('librarian/', librarian_dashboard, name='librarian_dashboard'),
    path('member/', member_dashboard, name='member_dashboard'),
]
