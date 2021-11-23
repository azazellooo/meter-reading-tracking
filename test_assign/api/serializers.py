from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Meter, History


class UserSerializer(serializers.HyperlinkedModelSerializer):
    meters = serializers.PrimaryKeyRelatedField(many=True, queryset=Meter)

    class Meta:
        model = User
        fields = ['id', 'username', 'meters']


class MeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meter
        fields = ('id', 'name', 'person', 'current_meter_reading')
        read_only_fields = ('id', 'person')


