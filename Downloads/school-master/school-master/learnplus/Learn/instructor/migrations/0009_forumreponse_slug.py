# Generated by Django 2.2.12 on 2024-12-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("instructor", "0008_auto_20241218_0902"),
    ]

    operations = [
        migrations.AddField(
            model_name="forumreponse",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
