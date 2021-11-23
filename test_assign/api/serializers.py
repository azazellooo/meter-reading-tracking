from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Meter, History


class UserSerializer(serializers.HyperlinkedModelSerializer):
    meters = serializers.PrimaryKeyRelatedField(many=True, queryset=Meter)

    class Meta:
        model = User
        fields = ['id', 'username', 'meters']


class MeterSerializer(serializers.ModelSerializer):
    history = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = Meter
        fields = ('id', 'name', 'person', 'current_meter_reading', 'history')
        read_only_fields = ('id', 'person')


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ['date', 'meter', 'meter_reading', 'consumption', 'type']

