"""from django.shortcuts import render"""
from rest_framework import generics
from .serializer import DescargasSerializer
from .models import Descarga


class DescargasListCreateView(generics.ListCreateAPIView):
    serializer_class= DescargasSerializer
    queryset = Descarga.objects.all()
    
class DescargasRetrieveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= DescargasSerializer
    queryset = Descarga.objects.all()
