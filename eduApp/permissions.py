from rest_framework import permissions




class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
            
        return request.user.is_superuser


class HasProfile(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        try:
            profile = request.user.profile
            return False
        except:
            return True


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user==obj.user



class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.profile==obj.teacher



class HasProfileOrNotAllow(permissions.BasePermission):
    def has_permission(self, request, view):
        
        try:
            profile = request.user.profile
            return True
        except:
            return False