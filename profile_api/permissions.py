from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit thier own profile"""

    #This function gets called every time an API is called
    #This function will return a boolean
    def has_object_permission(self, request, view, obj)-> bool:
        """Check user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS: #SAFE METHODS are methods that dont chanage anything like GET
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj)-> bool:
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id