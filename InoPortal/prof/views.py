from rest_framework import viewsets
from .serializers import StudentSerializer
from student.models import Student
# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    lookup_field = 'roll'
    serializer_class = StudentSerializer
