# from django.contrib.auth.models import User
# from django.db import models
#
# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# class Admin(AbstractUser):
#     is_superadmin = models.BooleanField(default=False)  #  distinguir superadmin
#     can_manage_users = models.BooleanField(default=True)
#     can_manage_spaces = models.BooleanField(default=True)
#     can_view_reports = models.BooleanField(default=True)
#
#     class Meta:
#         verbose_name = "Admin"
#         verbose_name_plural = "Admins"
#
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name="admin_user_set",  # Nombre único para evitar conflictos
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name="admin_user_set_permissions",  # Nombre único para evitar conflictos
#         blank=True
#     )
#
#
# '''
# class AdminProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_superadmin = models.BooleanField(default=False)
#     can_manage_users = models.BooleanField(default=True)
#     can_manage_spaces = models.BooleanField(default=True)
#     can_view_reports = models.BooleanField(default=True)
#
#     def __str__(self):
#         return f"{self.user.username} - Admin Profile"
#
#
# '''