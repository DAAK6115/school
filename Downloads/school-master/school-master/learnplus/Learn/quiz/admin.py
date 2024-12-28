from django.contrib import admin
from . import models

# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    actions = ("activate", "desactivate")
    list_filter = ("status",)
    list_per_page = 10
    date_hierachy = "date_add"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "la selection a été effectué avec succes")

    activate.short_description = "permet d'activer le champs selectionner"

    def desactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "la selection a été effectué avec succes")

    desactivate.short_description = "permet de desactiver le champs selectionner"


class QuestionAdmin(CustomAdmin):
    list_display = ("typequestion", "point")
    list_display_links = [
        "typequestion",
    ]
    search_fields = ("typequestion",)
    fieldsets = [
        ("info question", {"fields": ["typequestion", "point", "quiz", "question"]}),
        ("standard", {"fields": ["status"]}),
    ]


class ReponseAdmin(CustomAdmin):
    list_display = ("reponse", "question", "is_True", "status")
    list_display_links = [
        "reponse",
    ]
    search_fields = ("reponse",)
    fieldsets = [
        ("info reponse", {"fields": ["reponse", "question", "is_True"]}),
        ("standard", {"fields": ["status"]}),
    ]


class QuizAdmin(CustomAdmin):
    list_display = ("date", "titre", "temps", "status")
    list_display_links = [
        "titre",
    ]
    search_fields = ("titre",)
    fieldsets = [
        ("info quiz", {"fields": ["date", "titre", "cours", "temps"]}),
        ("standard", {"fields": ["status"]}),
    ]


class DevoirAdmin(CustomAdmin):
    list_display = (
        "dateDebut",
        "dateFermeture",
        "chapitre",
        "coefficient",
        "support",
        "status",
    )
    list_display_links = ("chapitre",)
    search_fields = ("chapitre",)
    fieldsets = [
        (
            "info devoir",
            {"fields": ["dateDebut", "dateFermeture", "chapitre", "support"]},
        ),
        ("standard", {"fields": ["status"]}),
    ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Question, QuestionAdmin)
_register(models.Reponse, ReponseAdmin)
_register(models.Quiz, QuizAdmin)
_register(models.Devoir, DevoirAdmin)
