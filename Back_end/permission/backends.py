from django.contrib.auth import backends, get_user_model
from django.contrib.auth.models import Permission


class IBASBackend(backends.ModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def _get_role_permissions(self, user_obj):
        user_roles_field = get_user_model()._meta.get_field('roles')
        user_groups_query = 'role__%s' % user_roles_field.related_query_name()
        return Permission.objects.filter(**{user_groups_query: user_obj})

    def get_role_permissions(self, user_obj, obj=None):
        """
        Return a set of auth strings the user `user_obj` has from their
        `user_permissions`.
        """
        return self._get_permissions(user_obj, obj, 'role')

    def get_all_permissions(self, user_obj, obj=None):
        return {
            *self.get_user_permissions(user_obj, obj=obj),
            *self.get_group_permissions(user_obj, obj=obj),
            *self.get_role_permissions(user_obj, obj=obj),
        }


