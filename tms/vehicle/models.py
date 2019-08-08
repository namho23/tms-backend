from django.db import models
from django.contrib.postgres.fields import ArrayField

from . import managers
from ..core import constants as c
from ..core.models import TimeStampedModel, ApprovedModel
from ..account.models import User


class Vehicle(TimeStampedModel):
    """
    Vehicle model
    """
    # Basic Information
    model = models.CharField(
        max_length=1,
        choices=c.VEHICLE_MODEL_TYPE,
        default=c.VEHICLE_MODEL_TYPE_TRUCK
    )

    plate_num = models.CharField(
        max_length=100,
        unique=True
    )

    identifier_code = models.CharField(
        max_length=100
    )

    brand = models.CharField(
        max_length=1,
        choices=c.VEHICLE_BRAND,
        default=c.VEHICLE_BRAND_TONGHUA
    )

    use_for = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    total_load = models.DecimalField(
        max_digits=c.WEIGHT_MAX_DIGITS,
        decimal_places=c.WEIGHT_DECIMAL_PLACES
    )

    actual_load = models.DecimalField(
        max_digits=c.WEIGHT_MAX_DIGITS,
        decimal_places=c.WEIGHT_DECIMAL_PLACES
    )

    affiliation_unit = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    use_started_on = models.DateField(
        null=True,
        blank=True
    )

    use_expires_on = models.DateField(
        null=True,
        blank=True
    )

    service_area = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    obtain_method = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    attribute = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    # Identity Information
    cert_type = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    cert_id = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    cert_authority = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    cert_registered_on = models.DateField(
        null=True,
        blank=True
    )

    cert_active_on = models.DateField(
        null=True,
        blank=True
    )

    cert_expires_on = models.DateField(
        null=True,
        blank=True
    )

    insurance_active_on = models.DateField(
        null=True,
        blank=True
    )

    insurance_expires_on = models.DateField(
        null=True,
        blank=True
    )

    # Position Information
    branches = ArrayField(
        models.PositiveIntegerField()
    )

    # Hardware Information
    engine_model = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    engine_power = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    transmission_model = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    engine_displacement = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    tire_rules = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    tank_material = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    is_gps_installed = models.BooleanField(
        default=False
    )

    is_gps_working = models.BooleanField(
        default=False
    )

    with_pump = models.BooleanField(
        default=False
    )

    main_car_size = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    main_car_color = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    trailer_car_size = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    trailer_car_color = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=1,
        choices=c.VEHICLE_STATUS,
        default=c.VEHICLE_STATUS_AVAILABLE
    )

    @property
    def branch_count(self):
        return len(self.branches)

    objects = models.Manager()
    inworks = managers.InWorkVehicleManager()
    availables = managers.AvailableVehicleManager()
    repairs = managers.RepairVehicleManager()

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.plate_num


class Tire(TimeStampedModel):

    model = models.CharField(
        max_length=100
    )

    tire_type = models.CharField(
        max_length=100
    )

    tread_depth = models.FloatField(
        default=0
    )

    mileage_limit = models.PositiveIntegerField(
        default=0
    )

    use_cycle = models.PositiveIntegerField(
        default=0
    )


class FuelConsumption(TimeStampedModel):

    vehicle_type = models.CharField(
        max_length=100
    )

    high_way = models.FloatField(
        default=0
    )

    normal_way = models.FloatField(
        default=0
    )

    description = models.TextField(
        null=True,
        blank=True
    )


class VehicleMaintenanceRequest(ApprovedModel):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=1,
        choices=c.VEHICLE_MAINTENANCE
    )

    maintenance_from = models.DateField()

    maintenance_to = models.DateField()

    class Meta:
        ordering = ['approved', '-approved_time', '-request_time']
        unique_together = ['vehicle', 'approved']


class VehicleCheckItem(TimeStampedModel):

    name = models.CharField(
        max_length=100
    )

    is_before_driving_item = models.BooleanField(
        default=False
    )

    is_driving_item = models.BooleanField(
        default=False
    )

    is_after_driving_item = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )


class VehicleBeforeDrivingCheckHistory(models.Model):

    driver = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    check_items = models.ManyToManyField(
        VehicleCheckItem,
        through='VehicleBeforeDrivingItemCheck',
        through_fields=('vehicle_check_history', 'item')
    )

    checked_time = models.DateTimeField(
        auto_now_add=True
    )


class VehicleBeforeDrivingItemCheck(models.Model):

    vehicle_check_history = models.ForeignKey(
        VehicleBeforeDrivingCheckHistory,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        VehicleCheckItem,
        on_delete=models.CASCADE
    )

    is_checked = models.BooleanField(
        default=False
    )


class VehicleDrivingCheckHistory(models.Model):

    driver = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    check_items = models.ManyToManyField(
        VehicleCheckItem,
        through='VehicleDrivingItemCheck',
        through_fields=('vehicle_check_history', 'item')
    )

    checked_time = models.DateTimeField(
        auto_now_add=True
    )


class VehicleDrivingItemCheck(models.Model):

    vehicle_check_history = models.ForeignKey(
        VehicleDrivingCheckHistory,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        VehicleCheckItem,
        on_delete=models.CASCADE
    )

    is_checked = models.BooleanField(
        default=False
    )


class VehicleAfterDrivingCheckHistory(models.Model):

    driver = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    check_items = models.ManyToManyField(
        VehicleCheckItem,
        through='VehicleAfterDrivingItemCheck',
        through_fields=('vehicle_check_history', 'item')
    )

    checked_time = models.DateTimeField(
        auto_now_add=True
    )


class VehicleAfterDrivingItemCheck(models.Model):

    vehicle_check_history = models.ForeignKey(
        VehicleAfterDrivingCheckHistory,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        VehicleCheckItem,
        on_delete=models.CASCADE
    )

    is_checked = models.BooleanField(
        default=False
    )
