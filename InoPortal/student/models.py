from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=15, blank=True)

    roll = models.TextField(max_length=10,
                            unique=True,
                            blank=True,
                            primary_key=True)

    regNo = models.TextField(max_length=10, blank=True)
    birthday = models.DateField(blank=True, null=True)
    club_name = models.TextField(max_length=30, blank=True, null=True)
    extra_curricular = models.TextField(max_length=30, blank=True, null=True)
    entry_time = models.DateTimeField(blank=True, null=True)
    laptop = models.CharField(max_length=10, blank=True, null=True)
    book1 = models.TextField(max_length=50, blank=True, null=True)
    book2 = models.TextField(max_length=50, blank=True, null=True)
    attendance = models.DateTimeField(blank=True, null=True)