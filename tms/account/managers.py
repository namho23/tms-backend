from django.db import models

from ..core import constants as c


class UserAdminManager(models.Manager):
    """
    Admin Model Manager
    """
    def get_queryset(self):
        return super().get_queryset().filter(role=c.USER_ROLE_ADMIN)


class UserStaffManager(models.Manager):
    """
    Staff Model Manager
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            role__in=[c.USER_ROLE_ADMIN, c.USER_ROLE_STAFF]
        )


class UserDriverManager(models.Manager):
    """
    Driver Model Manager
    """
    def get_queryset(self):
        return super().get_queryset().filter(role=c.USER_ROLE_DRIVER)


class UserEscortManager(models.Manager):
    """
    Escort Model Manager
    """
    def get_queryset(self):
        return super().get_queryset().filter(role=c.USER_ROLE_ESCORT)


class UserCustomerManager(models.Manager):
    """
    Customer Model Manager
    """
    def get_queryset(self):
        return super().get_queryset().filter(role=c.USER_ROLE_CUSTOMER)


class StaffStaffManager(models.Manager):
    """
    Driver staff manager
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            user__role__in=[c.USER_ROLE_ADMIN, c.USER_ROLE_STAFF]
        )


class StaffDriverManager(models.Manager):
    """
    Driver staff manager
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            user__role=c.USER_ROLE_DRIVER
        )


class StaffEscortManager(models.Manager):
    """
    Escort staff manager
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            user__role=c.USER_ROLE_ESCORT
        )