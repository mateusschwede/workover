from rest_framework import viewsets
from .models import Cafeteria
from .serializers import CafeteriaSerializer

class CafeteriaViewSet(viewsets.ModelViewSet):
    queryset = Cafeteria.objects.all()
    serializer_class = CafeteriaSerializer