# Generated by Django 2.2.13 on 2021-01-16 14:04
import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=2200)),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
            options={"ordering": ["-date_created"]},
        )
    ]
