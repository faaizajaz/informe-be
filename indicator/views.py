from django.shortcuts import render
from rest_framework.response import Response
from .models import Indicator, IndicatorEvidence
from rest_framework import generics, permissions
from rest_framework.parsers import FileUploadParser
from serializers.serializers import (
    IndicatorEvidenceSerializer,
    IndicatorViewSerializer,
    IndicatorCreateSerializer,
)


class IndicatorDetail(generics.RetrieveAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorViewSerializer


class IndicatorCreate(generics.CreateAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorCreateSerializer


class IndicatorEvidenceDetail(generics.RetrieveAPIView):
    queryset = IndicatorEvidence.objects.all()
    serializer_class = IndicatorEvidenceSerializer


class IndicatorEvidenceCreate(generics.CreateAPIView):
    queryset = IndicatorEvidence.objects.all()
    # serializer_class = IndicatorEvidenceSerializer
    parser_classes = [FileUploadParser]

    # def put(self, request, filename, format=None):
    #     print(request.data)
    #     return Response(status=204)
