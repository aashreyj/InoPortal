# Generated by Django 2.1.3 on 2019-08-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20190824_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='book1',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='book2',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
