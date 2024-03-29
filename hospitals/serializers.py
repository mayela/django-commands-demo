from rest_framework import serializers

from hospitals.models import Hospital


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('name', 'address', 'location', 'license')
