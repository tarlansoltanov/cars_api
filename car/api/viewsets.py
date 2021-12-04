from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from ..models import *
from .serializers import *

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=False)
    def popular(self, request):
        popular = Car.objects.all().annotate(rate_num=Count('rates')).order_by('-rate_num')
        serializer = self.get_serializer(popular, many=True, context={'popular' : True})
        return Response(serializer.data)
