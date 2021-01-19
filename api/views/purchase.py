from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from django_filters import rest_framework as filters

from api.serializers.purchase import PurchaseSerializer
from taxiadmin.models import Purchase

@authentication_classes([])
@permission_classes([])
class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('-id')
    serializer_class = PurchaseSerializer
    filterset_fields = ('OrderID', )

