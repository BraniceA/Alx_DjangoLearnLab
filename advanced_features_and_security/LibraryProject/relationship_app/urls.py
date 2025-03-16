# from django.urls import path
# from .views import list_books, LibraryDetailView, user_login, user_logout, register
# from django.contrib.auth.views import LoginView, LogoutView

# urlpatterns = [
#     path('books/', list_books, name='list_books'),
#     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
#     path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
#     path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
#     path("register/", register, name="register"),
# ]


from django.urls import path
from . import views  # Import views from the current module
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),  # Use views.register here
]