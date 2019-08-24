from rest_framework import serializers
from .models import Student


class LibStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'name',
            'roll',
            'entry_time',
            'laptop',
            'book1',
            'book2'
        ]
