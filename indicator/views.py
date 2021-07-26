from django.shortcuts import render
from .models import Indicator, IndicatorEvidence
from rest_framework import generics, permissions
from serializers.serializers import IndicatorSerializer


class IndicatorDetail(generics.RetrieveAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer


class IndicatorCreate(generics.CreateAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
