# Generated by Django 2.2.12 on 2024-12-10 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0004_student_bio"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="studentreponse",
            options={},
        ),
        migrations.RemoveField(
            model_name="studentreponse",
            name="date_update",
        ),
        migrations.RemoveField(
            model_name="studentreponse",
            name="is_True",
        ),
        migrations.RemoveField(
            model_name="studentreponse",
            name="reponse",
        ),
        migrations.AddField(
            model_name="studentreponse",
            name="answer",
            field=models.TextField(default="No answer provided"),
        ),
        migrations.AlterField(
            model_name="studentreponse",
            name="question",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="studentreponse",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student.Student"
            ),
        ),
    ]