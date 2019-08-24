from django.db import models

# Create your models here.


class Student(models.Model):
    """
    Student Model for Library Entrance
    """
    name = models.CharField(max_length=15, blank=True)

    roll = models.TextField(max_length=10,
                            unique=True,
                            blank=True,
                            primary_key=True)

    entry_time = models.DateTimeField(blank=True, null=True)
    laptop = models.CharField(max_length=10, blank=True, null=True)
    book1 = models.TextField(max_length=50, blank=True, null=True)
    book2 = models.TextField(max_length=50, blank=True, null=True)
