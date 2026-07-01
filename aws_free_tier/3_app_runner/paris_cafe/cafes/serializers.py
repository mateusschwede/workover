from rest_framework import serializers
from .models import Cafeteria

class CafeteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafeteria
        fields = '__all__'