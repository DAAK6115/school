# Generated by Django 2.2.8 on 2020-04-14 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("quiz", "0001_initial"),
        ("school", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("photo", models.ImageField(upload_to="images/Student")),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "classe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_classe",
                        to="school.Classe",
                    ),
                ),
                (
                    "filiere",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_filiere",
                        to="school.Filiere",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
            },
        ),
        migrations.CreateModel(
            name="StudentReponse",
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
                ("is_True", models.BooleanField()),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="StudentReponse_question",
                        to="quiz.Question",
                    ),
                ),
                (
                    "reponse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reponse_StudentReponse",
                        to="quiz.Reponse",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_studentreponse",
                        to="student.Student",
                    ),
                ),
            ],
            options={
                "verbose_name": "StudentReponse",
                "verbose_name_plural": "StudentReponses",
            },
        ),
    ]