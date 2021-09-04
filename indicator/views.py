from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response

from .models import Indicator, IndicatorEvidence
from .serializers import (
    IndicatorCreateSerializer,
    IndicatorEvidenceSerializer,
    IndicatorViewSerializer,
)


class IndicatorDetail(generics.RetrieveAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorViewSerializer


class IndicatorCreate(generics.CreateAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorCreateSerializer


# NOTE: create serializer is poorly named. It works here.
class IndicatorDelete(generics.DestroyAPIView):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorCreateSerializer


class IndicatorEvidenceDetail(generics.RetrieveAPIView):
    queryset = IndicatorEvidence.objects.all()
    serializer_class = IndicatorEvidenceSerializer


class IndicatorEvidenceCreate(generics.CreateAPIView):
    queryset = IndicatorEvidence.objects.all()
    serializer_class = IndicatorEvidenceSerializer
    parser_classes = [MultiPartParser, JSONParser]

    def post(self, request):
        evidence = IndicatorEvidence(
            name=request.data['name'], description=request.data['description']
        )
        evidence.save()

        if request.data['file'] != 'undefined':
            evidence.file = request.data['file']

        evidence.save()
        evidence.indicator.set([request.data['indicator']])
        evidence.save()
        return Response(status=204)
