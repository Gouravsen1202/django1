# Generated by Django 5.2.1 on 2025-05-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_items_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('item_des', models.CharField(max_length=20)),
                ('item_price', models.IntegerField()),
                ('item_quantity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
