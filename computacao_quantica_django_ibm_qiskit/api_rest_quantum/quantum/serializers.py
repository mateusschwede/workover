from rest_framework import serializers

class RandomBitResponseSerializer(serializers.Serializer):
    bit = serializers.IntegerField()
    backend = serializers.CharField()
    circuit = serializers.CharField()

class HealthResponseSerializer(serializers.Serializer):
    status = serializers.CharField()

class CoinFlipResponseSerializer(serializers.Serializer):
    result = serializers.CharField()
    backend = serializers.CharField()
    circuit = serializers.CharField()

class RandomNumberResponseSerializer(serializers.Serializer):
    bits = serializers.IntegerField()
    binary = serializers.CharField()
    decimal = serializers.IntegerField()
    backend = serializers.CharField()
    circuit = serializers.CharField()