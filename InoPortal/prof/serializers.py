from rest_framework import serializers
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name',
            'roll',
            'regNo',
            'birthday',
            'club_name',
            'extra_curricular'
        ]
