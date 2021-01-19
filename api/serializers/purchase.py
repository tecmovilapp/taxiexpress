from rest_framework import serializers

from taxiadmin.models import Purchase

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase        
        fields = ('id','MerID','AcqID','OrderID','ResponseCode','ReasonCode','ReasonCodeDesc','ReferenceNo','PaddedCardNo','AuthCode','CVV2Result','ShipToFirstName','ShipToLastName','ShipToCountry','ShipToEmail','OriginalResponseCode','Signature','SignatureMethod','RegisterDate')