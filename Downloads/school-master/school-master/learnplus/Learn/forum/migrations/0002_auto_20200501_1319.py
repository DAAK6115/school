# Generated by Django 2.2.8 on 2020-05-01 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sujet",
            name="cours",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cours_forum",
                to="school.Cours",
            ),
        ),
    ]
