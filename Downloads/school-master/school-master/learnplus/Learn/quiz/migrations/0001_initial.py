# Generated by Django 2.2.8 on 2020-04-14 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
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
                ("question", models.TextField(max_length=255)),
                ("point", models.IntegerField()),
                (
                    "typequestion",
                    models.CharField(
                        choices=[
                            ("qcm", "qcm"),
                            ("question-reponse", "question-reponse"),
                        ],
                        max_length=20,
                    ),
                ),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Question",
                "verbose_name_plural": "Questions",
            },
        ),
        migrations.CreateModel(
            name="Reponse",
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
                ("reponse", models.TextField(max_length=255)),
                ("is_True", models.BooleanField()),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question_reponse",
                        to="quiz.Question",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reponse",
                "verbose_name_plural": "Reponses",
            },
        ),
        migrations.CreateModel(
            name="Quiz",
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
                ("date", models.CharField(max_length=255)),
                ("titre", models.CharField(max_length=255)),
                ("temps", models.IntegerField()),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "cours",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quiz_cours",
                        to="school.Cours",
                    ),
                ),
            ],
            options={
                "verbose_name": "Quiz",
                "verbose_name_plural": "Quizs",
            },
        ),
        migrations.AddField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quiz_question",
                to="quiz.Quiz",
            ),
        ),
        migrations.CreateModel(
            name="Devoir",
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
                ("sujet", models.TextField(max_length=255)),
                ("dateDebut", models.DateTimeField()),
                ("dateFermeture", models.DateTimeField()),
                ("coefficient", models.IntegerField()),
                ("support", models.FileField(upload_to="fichier/import")),
                ("date_add", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=True)),
                (
                    "chapitre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quiz_chapitre",
                        to="school.Chapitre",
                    ),
                ),
            ],
            options={
                "verbose_name": "Devoir",
                "verbose_name_plural": "Devoirs",
            },
        ),
    ]
