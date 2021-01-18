from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes

from api.serializers.purchase import PurchaseSerializer
from taxiadmin.models import Purchase

@authentication_classes([])
@permission_classes([])
class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('RegisterDate')
    serializer_class = PurchaseSerializer