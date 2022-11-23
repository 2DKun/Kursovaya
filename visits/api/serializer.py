from rest_framework import serializers


class ApiSerializer(serializers.Serializer):
    req = serializers.CharField(max_length=255)
    res = serializers.CharField(max_length=1000)