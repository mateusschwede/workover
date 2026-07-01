from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HealthResponseSerializer, RandomBitResponseSerializer, CoinFlipResponseSerializer, RandomNumberResponseSerializer
from .services import QuantumService

class HealthCheckView(APIView):
    def get(self, request):
        data = QuantumService.health()
        serializer = HealthResponseSerializer(instance=data)
        return Response(serializer.data)

class RandomBitView(APIView):
    def get(self, request):
        data = QuantumService.generate_random_bit()
        serializer = RandomBitResponseSerializer(instance=data)
        return Response(serializer.data)
    
class CoinFlipView(APIView):
    def get(self, request):
        data = QuantumService.coin_flip()
        serializer = CoinFlipResponseSerializer(instance=data)
        return Response(serializer.data)
    
class RandomNumberView(APIView):
    def get(self, request):
        bits = int(request.query_params.get("bits", 8))
        data = QuantumService.generate_random_number(bits)
        serializer = RandomNumberResponseSerializer(instance=data)
        return Response(serializer.data)