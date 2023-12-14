from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    '''
    Check if authenticated user is seller(owner) of the product or admin
    '''

    messages = "test"

    def has_permission(self, request, view):
        return request.user.is_authenticated is True
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.seller == request.user or request.user.is_superuser