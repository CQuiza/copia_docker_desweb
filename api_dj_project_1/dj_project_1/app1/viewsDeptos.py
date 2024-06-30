from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

from .serializers import DeptosSerializer
from .models import Deptos

class DeptosViews(viewsets.ModelViewSet):
    serializer_class = DeptosSerializer
    queryset = Deptos.objects.all()
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):  

        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()