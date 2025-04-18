Provide a README file detailing the setup process, how to register and authenticate users, and a brief overview of the user model.

THE SETUP PROCESS...
I created a New Django Project

    Environment Setup:
        Created a new Django project named social_media_api:  django-admin startproject social_media_api
        Navigated into project directory and created a new Django app called accounts for handling user-related functionality: cd social_media_api python manage.py startapp accounts
        Added 'rest_framework' and 'accounts' to the INSTALLED_APPS in settings.py.

I configured User Authentication

    User Model and Authentication:
        Created a custom user model that extends Django’s AbstractUser, adding fields such as bio, profile_picture, and followers (a ManyToMany field referencing itself, symmetrical=False).
        Set up Django REST Framework’s token authentication by adding 'rest_framework.authtoken' to my installed apps and running migrations to create the token model.
        Implemented views and serializers in the accounts app for user registration, login, and token retrieval.

Defined URL Patterns

    Routing Configuration:
        I configured URL patterns in accounts/urls.py to include routes for registration (/register), login (/login), and user profile management (/profile).
        Ensured that registration and login endpoints return a token upon successful operations.

Testing and Initial Launch

    Server Testing:
        I started the Django development server to ensure the initial setup is configured correctly: python manage.py runserver
        I used Postman to test user registration and login functionalities, verifying that tokens are generated and returned correctly.

