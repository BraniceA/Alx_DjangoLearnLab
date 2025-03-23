# Django REST Framework Authentication Setup

## Authentication Used
- Token Authentication (`rest_framework.authentication.TokenAuthentication`)

## Steps to Generate and Use Tokens
1. Create a user using Django Admin or shell.
2. Run `python manage.py shell` and execute:
   ```python
   from django.contrib.auth.models import User
   from rest_framework.authtoken.models import Token
   user = User.objects.get(username="your_username")
   token, created = Token.objects.get_or_create(user=user)
   print(token.key)
