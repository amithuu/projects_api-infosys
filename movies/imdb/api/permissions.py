from rest_framework import permissions

class AdminOrReadonly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        # return bool(request.user and request.user.is_staff)
        admin_access = bool(request.user and request.user.is_staff)
        return admin_access or request.method == 'GET'
        