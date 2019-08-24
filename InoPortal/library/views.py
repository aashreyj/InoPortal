from rest_framework import viewsets
from .serializers import LibStudentSerializer
from .models import Student
from rest_framework.response import Response
# Create your views here.


class LibStudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    lookup_field = 'roll'
    serializer_class = LibStudentSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.entry_time = request.data.get("entry_time")
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.save()
        self.perform_update(serializer)
        return Response(serializer.data)
