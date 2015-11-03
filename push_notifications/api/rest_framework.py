from __future__ import absolute_import

from rest_framework import permissions, status
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.fields import IntegerField

from push_notifications.models import APNSDevice, GCMDevice
from push_notifications.fields import hex_re
from rest_framework.response import Response

# Fields

class HexIntegerField(IntegerField):
    """
    Store an integer represented as a hex string of form "0x01".
    """

    def to_internal_value(self, data):
        data = int(data, 16)
        return super(HexIntegerField, self).to_internal_value(data)

    def to_representation(self, value):
        return value


# Serializers
class DeviceSerializerMixin(ModelSerializer):
    class Meta:
        fields = ("name", "registration_id", "device_id", "active", "date_created")
        read_only_fields = ("date_created", )


class APNSDeviceSerializer(ModelSerializer):

    class Meta(DeviceSerializerMixin.Meta):
        model = APNSDevice

    def validate_registration_id(self, value):
        # iOS device tokens are 256-bit hexadecimal (64 characters)

        if hex_re.match(value) is None or len(value) != 64:
            raise ValidationError("Registration ID (device token) is invalid")

        return value


class GCMDeviceSerializer(ModelSerializer):
    device_id = HexIntegerField(
        help_text="ANDROID_ID / TelephonyManager.getDeviceId() (e.g: 0x01)",
        style={'input_type': 'text'},
        required=False
    )

    class Meta(DeviceSerializerMixin.Meta):
        model = GCMDevice


# Permissions
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # must be the owner to view the object
        return obj.user == request.user


# Mixins
class DeviceViewSetMixin(object):
    lookup_field = "registration_id"

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            serializer.save(user=self.request.user)


class AuthorizedMixin(object):
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        # filter all devices to only those belonging to the current user
        return self.queryset.filter(user=self.request.user)


# ViewSets
class APNSDeviceViewSet(DeviceViewSetMixin, ModelViewSet):
    queryset = APNSDevice.objects.all()
    serializer_class = APNSDeviceSerializer


class APNSDeviceAuthorizedViewSet(AuthorizedMixin, APNSDeviceViewSet):
    pass


class GCMDeviceViewSet(DeviceViewSetMixin, ModelViewSet):
    queryset = GCMDevice.objects.all()
    serializer_class = GCMDeviceSerializer

    def create(self, request, *args, **kwargs):
    	if 'device_id' in request.data:
    		device = GCMDevice.objects.filter(device_id=request.data['device_id'])
    	else:
    		device = []
        if len(device) == 0:
            serializer = GCMDeviceSerializer(data=request.data)
            if serializer.is_valid():
                s = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = GCMDeviceSerializer(device[0],data=request.data,partial=True)
            if serializer.is_valid():
                s = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GCMDeviceAuthorizedViewSet(AuthorizedMixin, GCMDeviceViewSet):
    pass
