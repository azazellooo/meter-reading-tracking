from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Meter
from .serializers import MeterSerializer
from .permissions import AdminOrOwnerPermission


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'meters': reverse('meters', request=request, format=format),
    })


class MeterViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = MeterSerializer
    permission_classes = [AdminOrOwnerPermission]
    queryset = Meter.objects.all()

    def perform_create(self, serializer):
        serializer.save(person=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return super(MeterViewSet, self).get_permissions()


class MeterDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = MeterSerializer
    queryset = Meter.objects.all()
    permission_classes = [AdminOrOwnerPermission]

    def get_object(self):
        meter = Meter.objects.get(id=self.kwargs.get('pk'))
        return meter

    def put(self, request, *args, **kwargs):
        meter = self.get_object()
        serializer = MeterSerializer(data=request.data)
        if serializer.is_valid():
            meter.person = request.user
            serializer.update(instance=meter, validated_data=request.data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        meter = self.get_object()
        self.perform_destroy(meter)
        return Response(status=status.HTTP_204_NO_CONTENT)

