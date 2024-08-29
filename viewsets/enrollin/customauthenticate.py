from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Retrieve the username from the query parameters
        username = request.GET.get("username")
        if not username:
            return None
        
        try:
            # Attempt to get the user from the database
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid username")
        
        # Return a tuple of the user and None (for the token)
        return (user, None)
