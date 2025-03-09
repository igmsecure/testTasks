from django.shortcuts import render
from rest_framework import viewsets
from .models import Letter, Package
from .serializers import LetterSerializer, PackageSerializer

class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

