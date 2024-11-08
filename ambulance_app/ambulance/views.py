from django.shortcuts import render
from rest_framework import viewsets
from .models import Ambulance, Request
from .serializers import AmbulanceSerializer, RequestSerializer

class AmbulanceViewSet(viewsets.ModelViewSet):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer