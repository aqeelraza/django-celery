from rest_framework import serializers


class SNSSerializer(serializers.Serializer):
    email = serializers.EmailField()


