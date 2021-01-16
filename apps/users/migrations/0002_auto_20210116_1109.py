# Generated by Django 2.2.13 on 2021-01-16 17:09
import imagefield.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image_height",
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="image_ppoi",
            field=imagefield.fields.PPOIField(default="0.5x0.5", max_length=20),
        ),
        migrations.AddField(
            model_name="profile",
            name="image_width",
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=imagefield.fields.ImageField(
                default="default.jpg",
                height_field="image_height",
                upload_to="profile_pics",
                width_field="image_width",
            ),
        ),
    ]
