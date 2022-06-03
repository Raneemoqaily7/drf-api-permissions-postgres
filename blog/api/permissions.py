from rest_framework import permissions



class OwnerLogin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated


        




class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True 

        if obj.owner is None :
            return True 
        

        return obj.author == request.user



class OwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.author == request.user


