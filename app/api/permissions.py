from operator import truediv
from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    """
    Permission for Admin user
    """
    def has_permission(self, request, view):
        if request.user.userprofile.user_type == 1:
            return True
        else:
            return False

class UserPermission(permissions.BasePermission):
    
    """Permission for a normal user
    """

    def has_permission(self, request, view):
        try:
            if request.user.userprofile.user_type == 2:
                return True
            else:
                return False
        except:
            return False
        
class RegisterPermission(permissions.BasePermission):
    """
    Not Register to the same 
    """

    def has_permission(self, request, view):
        try:
            if request.user.userprofile.user_type == 2:
                return True
            else:
                return False
        except:
            return False