#This function:
#    Checks if the logged-in user has a UserProfile and the required role.
#    Denies access if the role does not match.

from django.core.exceptions import PermissionDenied

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'userprofile') and request.user.userprofile.role == role:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied  # Returns a 403 Forbidden response
        return _wrapped_view
    return decorator

