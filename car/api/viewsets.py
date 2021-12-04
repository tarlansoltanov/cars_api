from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from ..models import *
from .serializers import *

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.action == 'rate':
            return RateSerializer
        return CarSerializer        


    @action(detail=True, methods=['post'])
    def rate(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False)
    def popular(self, request):
        popular = Car.objects.all().annotate(rate_num=Count('rates')).order_by('-rate_num')
        serializer = self.get_serializer(popular, many=True, context={'popular' : True})
        return Response(serializer.data)
