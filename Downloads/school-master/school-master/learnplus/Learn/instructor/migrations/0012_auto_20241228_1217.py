# Generated by Django 2.2.12 on 2024-12-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("instructor", "0011_privatemessage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instructor",
            name="photo",
            field=models.ImageField(
                default="github.png", upload_to="images/Instructor"
            ),
        ),
    ]
