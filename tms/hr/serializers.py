from django.shortcuts import get_object_or_404
from rest_framework import serializers

from . import models as m
from ..core import constants as c

# models
from ..account.models import User
from ..info.models import Product

# serializers
from ..core.serializers import TMSChoiceField
from ..account.serializers import (
    ShortUserSerializer, MainUserSerializer, UserSerializer,
    DriverAppUserSerializer
)
from ..info.serializers import ShortProductSerializer


class ShortDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Department
        fields = (
            'id', 'name'
        )


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Department
        fields = '__all__'


class ShortPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Position
        fields = (
            'id', 'name'
        )


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Position
        fields = '__all__'


class RoleManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.RoleManagement
        fields = '__all__'


class RoleManagementDataViewSerializer(serializers.ModelSerializer):

    department = ShortDepartmentSerializer()
    position = ShortPositionSerializer()

    class Meta:
        model = m.RoleManagement
        fields = '__all__'


class DriverLicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.DriverLicense
        fields = '__all__'


class ShortStaffProfileSerializer(serializers.ModelSerializer):

    name = serializers.CharField(source='user.name')

    class Meta:
        model = m.StaffProfile
        fields = (
            'id', 'name'
        )


class DriverAppStaffProfileSerializer(serializers.ModelSerializer):

    department = ShortDepartmentSerializer(read_only=True)
    position = ShortPositionSerializer(read_only=True)
    user = DriverAppUserSerializer(read_only=True)

    class Meta:
        model = m.StaffProfile
        fields = (
            'id', 'user', 'department', 'position'
        )


class StaffProfileSerializer(serializers.ModelSerializer):

    department = ShortDepartmentSerializer(read_only=True)
    position = ShortPositionSerializer(read_only=True)

    class Meta:
        model = m.StaffProfile
        fields = '__all__'
        read_only_fields = ('user', 'driver_license')

    def create(self, validated_data):
        # get user data and create
        user_data = self.context.get('user', None)
        if user_data is None:
            raise serializers.ValidationError({
                'user': 'User data is not provided'
            })

        # check if username and mobile exists already
        if m.User.objects.filter(username=user_data['username']).exists():
            raise serializers.ValidationError({
                'username': 'Such user already exists'
            })

        if m.User.objects.filter(mobile=user_data['mobile']).exists():
            raise serializers.ValidationError({
                'mobile': 'Such mobile already exisits'
            })

        # check user role
        user_data['role'] = user_data['role']['value']
        user = m.User.objects.create_user(**user_data)

        department_data = self.context.get('department', None)
        department = get_object_or_404(
            m.Department,
            id=department_data.get('id', None)
        )

        position_data = self.context.get('position', None)
        position = get_object_or_404(
            m.Position,
            id=position_data.get('id', None)
        )

        driver_license = self.context.get('driver_license', None)
        if driver_license is not None:
            driver_license = m.DriverLicense.objects.create(
                **driver_license
            )

        profile = m.StaffProfile.objects.create(
            user=user,
            department=department,
            position=position,
            **validated_data
        )
        return profile

    def update(self, instance, validated_data):
        user_data = self.context.get('user', None)
        if user_data is None:
            raise serializers.ValidationError({
                'user': 'User data is not provided'
            })

        # check if username and mobile exists already
        if m.User.objects.exclude(pk=instance.user.id).filter(
            username=user_data['username']
        ).exists():
            raise serializers.ValidationError({
                'username': 'Such user already exists'
            })

        if m.User.objects.exclude(pk=instance.user.id).filter(
            mobile=user_data['mobile']
        ).exists():
            raise serializers.ValidationError({
                'mobile': 'Such mobile already exisits'
            })

        password = user_data.pop('password', None)
        if password is not None:
            instance.user.set_password(password)

        user_data['role'] = user_data['role']['value']
        for (key, value) in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()

        department_data = self.context.get('department', None)
        department = get_object_or_404(
            m.Department,
            id=department_data.get('id', None)
        )

        position_data = self.context.get('position', None)
        position = get_object_or_404(
            m.Position,
            id=position_data.get('id', None)
        )

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.department = department
        instance.position = position
        instance.save()

        return instance

    def to_internal_value(self, data):
        """
        Exclude date, datetimefield if its string is empty
        """
        for key, value in self.fields.items():
            if isinstance(value, serializers.DateField) and data[key] == '':
                data.pop(key)

        ret = super().to_internal_value(data)
        return ret


class StaffProfileDataViewSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    department = ShortDepartmentSerializer()
    position = ShortPositionSerializer()
    driver_license = DriverLicenseSerializer()

    class Meta:
        model = m.StaffProfile
        fields = '__all__'


class ShortCustomerProfileSerializer(serializers.ModelSerializer):

    user_id = serializers.CharField(source='user.id')
    name = serializers.CharField(source='user.name')
    mobile = serializers.CharField(source='user.mobile')

    class Meta:
        model = m.CustomerProfile
        fields = (
            'id', 'user_id', 'name', 'mobile'
        )


class CustomerProfileSerializer(serializers.ModelSerializer):

    user = MainUserSerializer(read_only=True)
    associated_with = ShortUserSerializer(read_only=True)
    products = ShortProductSerializer(many=True, read_only=True)
    payment_method = TMSChoiceField(choices=c.PAYMENT_METHOD)

    class Meta:
        model = m.CustomerProfile
        fields = '__all__'
        read_only_fields = ('user', 'products')

    def create(self, validated_data):
        user_data = self.context.get('user', None)
        if user_data is None:
            raise serializers.ValidationError({
                'user': 'User data is not provided'
            })

        # check if username and mobile exists already
        if m.User.objects.filter(username=user_data['username']).exists():
            raise serializers.ValidationError({
                'username': 'Such user already exists'
            })

        associated_with = self.context.get('associated_with', None)
        if associated_with is None:
            raise serializers.ValidationError({
                'associated_with': 'Associated data are missing'
            })

        associated_id = associated_with.get('id', None)
        try:
            associated_with = m.User.objects.get(id=associated_id)
        except m.User.objects.DoesNotExist:
            raise serializers.ValidationError({
                'associated_with': 'Such user does not exist'
            })

        products_data = self.context.get('products', None)
        if products_data is None:
            raise serializers.ValidationError({
                'product': 'Product data is not provided'
            })

        user_data.setdefault('role', c.USER_ROLE_CUSTOMER)
        user = m.User.objects.create_user(**user_data)
        customer = m.CustomerProfile.objects.create(
            user=user,
            associated_with=associated_with,
            **validated_data
        )

        for product_data in products_data:
            product_id = product_data.get('id', None)
            try:
                product = Product.objects.get(pk=product_id)
                customer.products.add(product)
            except Product.DoesNotExist:
                pass

        return customer

    def update(self, instance, validated_data):
        # get user data and update
        user_data = self.context.get('user', None)
        if user_data is None:
            raise serializers.ValidationError({
                'user': 'User Data is not provided'
            })
        user = instance.user

        # check if user id exists already
        if m.User.objects.exclude(pk=user.id).filter(
            username=user_data['username']
        ).exists():
            raise serializers.ValidationError({
                'username': 'Such user already exists'
            })

        user.username = user_data.get('username', user.username)
        user.set_password(user_data.get('password', user.password))
        user.save()

        associated_with = self.context.get('associated_with', None)
        if associated_with is None:
            raise serializers.ValidationError({
                'associated_with': 'Associated data are missing'
            })

        associated_id = associated_with.get('id', None)
        try:
            associated_with = m.User.objects.get(id=associated_id)
        except m.User.objects.DoesNotExist:
            raise serializers.ValidationError({
                'associated_with': 'Such user does not exist'
            })

        instance.associated_with = associated_with
        products_data = self.context.get('products', None)
        if products_data is None:
            raise serializers.ValidationError({
                'product': 'Product data is not provided'
            })

        instance.products.clear()
        for product_data in products_data:
            product_id = product_data.get('id', None)
            try:
                product = Product.objects.get(pk=product_id)
                instance.products.add(product)
            except Product.DoesNotExist:
                pass

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class RestRequestSerializer(serializers.ModelSerializer):

    user = ShortUserSerializer(read_only=True)
    category = TMSChoiceField(choices=c.REST_REQUEST_CATEGORY)

    class Meta:
        model = m.RestRequest
        fields = '__all__'

    def create(self, validated_data):
        try:
            user_id = self.context.pop('user')
            user = User.companymembers.get(pk=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'user': 'User does not exist'
            })

        return m.RestRequest.objects.create(
            user=user,
            **validated_data
        )

    def update(self, instance, validated_data):
        user_id = self.context.pop('user')
        try:
            user_id = self.context.pop('user')
            user = User.companymembers.get(pk=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'user': 'User does not exist'
            })

        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.user = user
        instance.save()
        return instance

    def validate(self, data):
        from_date = data.get('from_date', None)
        to_date = data.get('to_date', None)

        if from_date > to_date:
            raise serializers.ValidationError({
                'to_date': 'Error'
            })

        return data
