
 

from django.shortcuts import render
from rest_framework import viewsets
from api_app.models import MatrixSoft, TrioCompany
from api_app.serializer import TrioCompanyserializer,MatrixSoftserializer


# Create your views here.

class TrioCompanyViewSet(viewsets.ModelViewSet):
        queryset=TrioCompany.objects.all()
        serializer_class=TrioCompanyserializer
        
            
        
        
class MatrixSoftViewSet(viewsets.ModelViewSet):
        queryset=MatrixSoft.objects.all()
        serializer_class=MatrixSoftserializer
                
        
        
        
        
        
        
        
        
        
        
        
        
        