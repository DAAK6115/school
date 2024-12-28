# Generated by Django 2.2.8 on 2020-04-20 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0002_auto_20200420_2227"),
        ("school", "0002_auto_20200420_1839"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="classe",
            name="filiere",
        ),
        migrations.RemoveField(
            model_name="matiere",
            name="coefficient",
        ),
        migrations.RemoveField(
            model_name="matiere",
            name="filiere",
        ),
        migrations.AlterField(
            model_name="cours",
            name="chapitre",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cours_chapitre",
                to="school.Chapitre",
            ),
        ),
        migrations.DeleteModel(
            name="Filiere",
        ),
    ]
