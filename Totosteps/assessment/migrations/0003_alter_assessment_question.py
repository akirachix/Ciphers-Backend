# Generated by Django 4.2.16 on 2024-09-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='question',
            field=models.JSONField(unique=True),
        ),
    ]
