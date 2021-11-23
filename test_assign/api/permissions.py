from rest_framework.permissions import IsAdminUser


class AdminOrOwnerPermission(IsAdminUser):

    def has_object_permission(self, request, view, obj):
        perm = super(AdminOrOwnerPermission, self).has_object_permission(request, view, obj)
        return perm or request == obj.person or view.action in ('destroy', 'update')
