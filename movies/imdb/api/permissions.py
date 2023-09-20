from rest_framework import permissions

class AdminOrReadonly(permissions.IsAdminUser):

    # def has_permission(self, request, view):
    #     # return bool(request.user and request.user.is_staff)
    #     admin_access = bool(request.user and request.user.is_staff)
    #     return admin_access or request.method == 'GET'
    
    # another way as well 

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
    
class ReviewUserOrReadonly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:  # [SAFE_METHODS== request.method == 'GET'] 
            return True
        else:
            return obj.review_user == request.user
        
    # this is the explanation of above function 
    # if request.method == 'GET':
        # return True  : user can only view the Data 
    #   else:
    #     return user_id.review_user == request.current_user [he can edit as well]