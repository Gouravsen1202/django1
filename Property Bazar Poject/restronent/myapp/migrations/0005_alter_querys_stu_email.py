# Generated by Django 5.2 on 2025-05-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_query_querys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querys',
            name='stu_email',
            field=models.EmailField(max_length=254),
        ),
    ]
