
#Import 
from rest_framework import serializers

from .models import TrioCompany,MatrixSoft


#Create All serializer here...!

class TrioCompanyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=TrioCompany
        fields="__all__"


class MatrixSoftserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MatrixSoft
        fields= "__all__"
        























