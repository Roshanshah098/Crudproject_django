from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        # Allow GET requests for everyone
        if request.method == 'GET':
            return True
        
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a staff member
        if not request.user.is_staff:
            return False
        
        return False  # or True, depending on  logic
