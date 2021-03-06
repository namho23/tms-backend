from django.db import models

from ..core import constants as c


class AvailableVehicleManager(models.Manager):
    """
    Manager for getting avaiable vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            status=c.VEHICLE_STATUS_AVAILABLE
        )


class UnderWheelVehicleManager(models.Manager):
    """
    Manager for getting in work vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            status=c.VEHICLE_STATUS_UNDER_WHEEL
        )


class RepairVehicleManager(models.Manager):
    """
    Manager for getting in repairing vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            status=c.VEHICLE_STATUS_REPAIR
        )


class BeforeDrivingCheckItemsManager(models.Manager):
    """
    Manager for getting in repairing vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            is_before_driving_item=True
        )


class DrivingCheckItemsManager(models.Manager):
    """
    Manager for getting in repairing vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            is_driving_item=True
        )


class AfterDrivingCheckItemsManager(models.Manager):
    """
    Manager for getting in repairing vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            is_after_driving_item=True
        )


class PublishedBeforeDrivingCheckItemsManager(models.Manager):
    """
    Manager for getting in repairing vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            is_before_driving_item=True,
            is_published=True
        )


class PublishedDrivingCheckItemsManager(models.Manager):
    """
    Manager for getting in repairing vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            is_driving_item=True,
            is_published=True
        )


class PublishedAfterDrivingCheckItemsManager(models.Manager):
    """
    Manager for getting in repairing vehicles
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            is_after_driving_item=True,
            is_published=True
        )


class VehicleDriverBindManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(
            worker_type=c.WORKER_TYPE_DRIVER
        )


class VehicleEscortBindManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(
            worker_type=c.WORKER_TYPE_ESCORT
        )
