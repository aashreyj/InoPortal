from rest_framework import viewsets
from .serializers import AttendanceSerializer, PermissionSerializer
from student.models import Student
from rest_framework.response import Response
from datetime import datetime
# Create your views here.


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    lookup_field = 'roll'
    serializer_class = AttendanceSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.attendance = datetime.now()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.save()
        self.perform_update(serializer)
        return Response(serializer.data)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    lookup_field = 'roll'
    serializer_class = PermissionSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.venue = request.data.get('venue')
        instance.datePermission = request.data.get('datePermission')
        instance.purpose = request.data.get('purpose')
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.save()
        self.perform_update(serializer)
        return Response(serializer.data)
