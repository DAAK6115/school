# Generated by Django 2.2.12 on 2024-12-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0005_auto_20241210_1848"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="photo",
            field=models.ImageField(default="github.png", upload_to="images/Student"),
        ),
    ]