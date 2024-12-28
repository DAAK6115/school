# Generated by Django 2.2.8 on 2020-04-20 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0003_auto_20200420_2227"),
        ("instructor", "0002_auto_20200417_1840"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instructor",
            name="matiere",
        ),
        migrations.AddField(
            model_name="instructor",
            name="classe",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="instructor_classe",
                to="school.Classe",
            ),
        ),
    ]
