from perpustakaan.models import Kelompok
from perpustakaan.serializers import KelompokSerializer
from rest_framework import viewsets, permissions

class KelompokViewset(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all()
    serializer_class = KelompokSerializer
    permission_classes = [permissions.IsAuthenticated]