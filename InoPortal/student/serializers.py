from rest_framework import serializers
from student.models import Student


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name',
            'roll',
            'attendance'
        ]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name',
            'regNo',
            'club_name',
            'venue',
            'purpose',
            'datePermission'
        ]
