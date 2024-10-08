# Generated by Django 4.2.16 on 2024-10-03 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("child", "0005_remove_child_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="child",
            name="parent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
