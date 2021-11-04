from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from IBAS import settings


class RoleManager(models.Manager):
    """
    The manager for the custom Role model.
    """
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Role(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissions'),
        blank=True,
    )

    objects = RoleManager()

    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name, )


# class AccountEmailaddress(models.Model):
#     email = models.CharField(unique=True, max_length=254)
#     verified = models.IntegerField()
#     primary = models.IntegerField()
#     user = models.ForeignKey(settings.base.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#     class Meta:
#         managed = False
#         db_table = 'account_emailaddress'
#
#
# class AccountEmailconfirmation(models.Model):
#     created = models.DateTimeField()
#     sent = models.DateTimeField(blank=True, null=True)
#     key = models.CharField(unique=True, max_length=64)
#     email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'account_emailconfirmation'
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


class AuthUser(AbstractUser):
    student_id = models.IntegerField(db_column='student_id', unique=True, null=True, blank=True)
    roles = models.ManyToManyField(
        Role,
        db_column='roles',
        verbose_name=_('roles'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their roles.'
        ),
        related_name="user_set",
        related_query_name="user",)

    class Meta:
        managed = False
        db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(settings.base.AUTH_USER_MODEL, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(settings.base.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class AuthRolePermissions(models.Model):
#     role = models.ForeignKey(Role,  on_delete=models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, on_delete=models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_role_permissions'
#         unique_together = (('role', 'permission'),)


# class AuthUserRoles(models.Model):
#     role = models.ForeignKey(Role, db_column='role_id', on_delete=models.DO_NOTHING)
#     user = models.ForeignKey(settings.base.AUTH_USER_MODEL, db_column='user_id', on_delete=models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_role'
#         unique_together = (('user', 'role'),)


# class DjangoSite(models.Model):
#     domain = models.CharField(unique=True, max_length=100)
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'django_site'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(settings.base.AUTH_USER_MODEL, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class SocialaccountSocialaccount(models.Model):
#     provider = models.CharField(max_length=30)
#     uid = models.CharField(max_length=191)
#     last_login = models.DateTimeField()
#     date_joined = models.DateTimeField()
#     extra_data = models.TextField()
#     user = models.ForeignKey(settings.base.AUTH_USER_MODEL, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'socialaccount_socialaccount'
#         unique_together = (('provider', 'uid'),)
#
#
# class SocialaccountSocialapp(models.Model):
#     provider = models.CharField(max_length=30)
#     name = models.CharField(max_length=40)
#     client_id = models.CharField(max_length=191)
#     secret = models.CharField(max_length=191)
#     key = models.CharField(max_length=191)
#
#     class Meta:
#         managed = False
#         db_table = 'socialaccount_socialapp'
#
#
# class SocialaccountSocialappSites(models.Model):
#     socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
#     site = models.ForeignKey(DjangoSite, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'socialaccount_socialapp_sites'
#         unique_together = (('socialapp', 'site'),)
#
#
# class SocialaccountSocialtoken(models.Model):
#     token = models.TextField()
#     token_secret = models.TextField()
#     expires_at = models.DateTimeField(blank=True, null=True)
#     account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
#     app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'socialaccount_socialtoken'
#         unique_together = (('app', 'account'),)

# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class SocialLoginBlog(models.Model):
#     text = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'social_login_blog'
