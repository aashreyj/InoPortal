# Generated by Django 2.1.3 on 2019-08-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(blank=True, max_length=15)),
                ('roll', models.TextField(blank=True, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('regNo', models.TextField(blank=True, max_length=10)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('club_name', models.TextField(blank=True, max_length=30, null=True)),
                ('extra_curricular', models.TextField(blank=True, max_length=30, null=True)),
                ('entry_time', models.DateTimeField(blank=True, null=True)),
                ('laptop', models.CharField(blank=True, max_length=10, null=True)),
                ('book1', models.TextField(blank=True, max_length=50, null=True)),
                ('book2', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
