from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school import models as school_models
from quiz import models as quiz_models
from forum import models as forum_models
from chat import models as chat_models
from . import models
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import ForumQuestion
from django.shortcuts import get_object_or_404
from forum.models import Sujet
from forum.models import Reponse
from django.contrib import messages


# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    try:
        if hasattr(request.user, "student_user"):
            # Redirige vers le tableau de bord étudiant
            return redirect("student-dashboard")
        elif hasattr(request.user, "instructor"):
            matiere = school_models.Matiere.objects.filter(status=True)
            datas = {
                "matiere": matiere,
            }
            return render(request, "pages/instructor-dashboard.html", datas)
        else:
            # Si aucun rôle n'est associé, redirige vers une page d'erreur ou connexion
            messages.error(request, "Votre compte n'est pas associé à un rôle valide.")
            return redirect("guest-login")
    except Exception as e:
        print(f"Error in dashboard view: {e}")
        messages.error(request, "Une erreur inattendue s'est produite.")
        return redirect("admin/")


@login_required(login_url="login")
def account_edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {}
                return render(request, "pages/instructor-account-edit.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


# @login_required(login_url = 'login')
# def browse_courses(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                 return render(request,'pages/instructor-browse-courses.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")


# @login_required(login_url = 'login')
# def carts(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                 return render(request,'pages/instructor-cart.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def course_add(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")

                if request.user.instructor:
                    matiere = school_models.Matiere.objects.filter(status=True)
                    datas = {
                        "matiere": matiere,
                    }
                    return render(request, "pages/instructor-course-add.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def course_edit(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")

                if request.user.instructor:
                    matiere = school_models.Matiere.objects.filter(status=True)
                    chapitre = school_models.Chapitre.objects.get(slug=slug)

                    datas = {
                        "matiere": matiere,
                        "chapitre": chapitre,
                    }
                    return render(request, "pages/instructor-course-edit.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def courses(request):
    if request.user.is_authenticated:
        try:
            instructor = request.user.instructor
            if not instructor.classe:  # Vérifie si une classe est associée
                return render(
                    request,
                    "pages/instructor-courses.html",
                    {
                        "error_message": "Vous n'avez pas encore de classe associée. "
                        "Veuillez contacter l'administration."
                    },
                )

            Chapitre = school_models.Chapitre.objects.filter(
                Q(status=True) & Q(classe=instructor.classe)
            )
            datas = {
                "Chapitre": Chapitre,
            }
            return render(request, "pages/instructor-courses.html", datas)
        except Exception as e:
            print(e)
            return redirect("/admin/")


@login_required(login_url="login")
def matiere(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    Chapitre = school_models.Chapitre.objects.filter(
                        Q(status=True)
                        & Q(classe=request.user.instructor.classe)
                        & Q(matiere__slug=slug)
                    )
                    datas = {
                        "Chapitre": Chapitre,
                    }
                    return render(request, "pages/instructor-cours-chap.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def earnings(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {}
                    return render(request, "pages/instructor-account-edit.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


# @login_required(login_url = 'login')
# def edit_invoice(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-edit-invoice.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def forum(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    forum_general = forum_models.Sujet.objects.filter(cours=None)
                    forum = forum_models.Sujet.objects.filter(
                        cours__chapitre__classe=request.user.instructor.classe
                    )
                    datas = {
                        "forum_general": forum_general,
                        "forum": forum,
                    }
                    return render(request, "pages/instructor-forum.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def forum_ask(request):
    if request.method == "POST":
        # Récupérez les données du formulaire
        title = request.POST.get("title")
        details = request.POST.get("details")
        topic = request.POST.get("topic")
        notify = request.POST.get("notify", False)  # Checkbox

        # Validation des données
        if not title or not details or not topic:
            messages.error(request, "All fields are required!")
            return redirect("instructor-forum-ask")

        try:
            # Enregistrez la question dans la base de données
            ForumQuestion.objects.create(
                title=title,
                details=details,
                topic=topic,
                user=request.user,
                notify=bool(notify),
            )
            messages.success(request, "Your question has been posted successfully!")
            return redirect("forum")  # Redirigez vers la page du forum
        except Exception as e:
            print("Error saving question:", e)
            messages.error(request, "An error occurred while posting your question.")
            return redirect("instructor-forum-ask")

    # Si méthode GET, affichez le formulaire
    return render(request, "pages/instructor-forum-ask.html")


@login_required(login_url="login")
def forum_thread(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    forum = forum_models.Sujet.objects.get(slug=slug)
                    datas = {
                        "forum": forum,
                    }
                    return render(request, "pages/instructor-forum-thread.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


# @login_required(login_url = 'login')
# def invoice(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-invoice.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


# @login_required(login_url = 'login')
# def invoice_settings(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(
#                  request,'pages/instructor-invoice-settings.html',
#                  datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def lesson_add(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    chapitre = school_models.Chapitre.objects.get(slug=slug)
                    datas = {
                        "chapitre": chapitre,
                    }
                    return render(request, "pages/instructor-lesson-add.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def lesson_edit(request, slug, id):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    chapitre = school_models.Chapitre.objects.get(id=id)
                    cours = school_models.Cours.objects.get(slug=slug)

                    datas = {
                        "chapitre": chapitre,
                        "cours": cours,
                    }
                    return render(request, "pages/instructor-lesson-edit.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def instructor_messages(request, classe):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    exist_classe = chat_models.Salon.objects.get(
                        classe=request.user.instructor.classe
                    )
                    info = school_models.Classe.objects.get(
                        id=request.user.instructor.classe.id
                    )
                    user_room = ""
                    print(user_room)
                    datas = {
                        "info_classe": info,
                        "classe": exist_classe,
                        "classe_json": mark_safe(json.dumps(exist_classe.id)),
                        "username": mark_safe(json.dumps(request.user.username)),
                    }
                    return render(request, "pages/instructor-messages.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


# @login_required(login_url = 'login')
# def messages_2(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-messages-2.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


# @login_required(login_url = 'login')
# def my_courses(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-my-courses.html',datas)
#         except Exception as e:
# print(e)
#             print("3")


@login_required(login_url="login")
def profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {}
                    return render(request, "pages/instructor-profile.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def quiz_edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {}
                    return render(request, "pages/instructor-quiz-edit.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def quiz_add(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {}
                    return render(request, "pages/instructor-quiz-add.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


# @login_required(login_url = 'login')
# def quiz_results(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-quiz-results.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def quizzes(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {}
                    return render(request, "pages/instructor-quizzes.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def review_quiz(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {}
                    return render(request, "pages/instructor-review-quiz.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def review_quiz_detail(request, quiz_id):
    try:
        quiz = quiz_models.Quiz.objects.get(id=quiz_id)
        return render(request, "pages/instructor-review-quiz.html", {"quiz": quiz})
    except quiz_models.Quiz.DoesNotExist:
        return redirect("instructor-dashboard")


@csrf_exempt
@login_required(login_url="login")
def save_review(request):
    if request.method == "POST":
        quiz_id = request.POST.get("quiz_id")
        score = request.POST.get("score")
        comment = request.POST.get("comment")

        try:
            quiz = quiz_models.Quiz.objects.get(id=quiz_id)
            # Mettez à jour les champs pertinents dans votre modèle Quiz ou Review
            quiz.score = score
            quiz.comment = comment
            quiz.save()
            return JsonResponse(
                {"success": True, "message": "Review saved successfully."}
            )
        except quiz_models.Quiz.DoesNotExist:
            return JsonResponse({"success": False, "message": "Quiz not found."})

    return JsonResponse({"success": False, "message": "Invalid request method."})


# @login_required(login_url='login')
# def take_course(request):
#    if request.user.is_authenticated:
#        try:
#            if hasattr(request.user, 'student_user'):
#                return redirect('index_student')
#        except Exception as e:
#            print("Erreur pour étudiant :", e)
#
#        try:
#            if hasattr(request.user, 'instructor'):
#                datas = {}
#                return render(request, 'pages/instructor-take-course.html', datas)
#        except Exception as e:
#            print("Erreur pour instructeur :", e)
#            return redirect("/admin/")
#    return redirect('login')  # Redirige vers login si non authentifié


@login_required(login_url="login")
def take_course(request):
    try:
        # Vérifie si l'utilisateur est un étudiant
        if hasattr(request.user, "student_user"):
            return redirect("index_student")

        # Vérifie si l'utilisateur est un instructeur
        if hasattr(request.user, "instructor"):
            context = {
                "course_title": "Vue.js Introduction",
                "instructor_name": "Adrian Demian",
                "start_date": "January 10, 2024",
                "end_date": "March 10, 2024",
                "course_description": (
                    "This course provides an in-depth introduction to Vue.js,"
                    "covering components, directives, "
                    "Vue Router, and state management with Vuex."
                    "Learn how to build modern and dynamic single-page applications."
                ),
                "chapters": [
                    {"title": "Introduction to Vue.js", "status": "Completed"},
                    {"title": "Components and Directives", "status": "In Progress"},
                    {"title": "Vue Router and SPA", "status": "Pending"},
                    {"title": "State Management with Vuex", "status": "Pending"},
                ],
            }
            return render(request, "pages/instructor-take-course.html", context)

        # Si l'utilisateur n'a pas de rôle valide
        return redirect("login")

    except Exception as e:
        print(f"Erreur lors de la gestion de l'utilisateur : {e}")
        return redirect("/admin/")


# @login_required(login_url = 'login')
# def take_quiz(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-take-quiz.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")


# @login_required(login_url = 'login')
# def view_course(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.student_user:
#                     return redirect('index_student')
#             except Exception as e:
# print(e)
#                 print("2")
#                 if request.user.instructor:
#                     datas = {

#                            }
#                     return render(request,'pages/instructor-view-course.html',datas)
#         except Exception as e:
# print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def statement(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect("index_student")
            except Exception as e:
                print(e)
                print("2")
                if request.user.instructor:
                    datas = {}
                    return render(request, "pages/instructor-statement.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


# fonction pour recuperer les donnees d'un cours et enregistrer


""" Add and update chapitre """


def post_cours(request):
    title = request.POST.get("title")
    matiere = request.POST.get("matiere")
    date_fin = request.POST.get("date_fin")
    description = request.POST.get("description")
    date_debut = request.POST.get("date_debut")
    duration = request.POST.get("duration")
    id = request.POST.get("id")
    chapitre = ""

    try:
        chapitre = school_models.Chapitre.objects.get(id=id)
        chapitre.titre = title
        chapitre.duree_en_heure = duration
        chapitre.description = description
        matiere = school_models.Matiere.objects.get(id=int(matiere))
        chapitre.matiere = matiere
        chapitre.classe = request.user.instructor.classe
        chapitre.save()

        try:
            video = request.FILES.get("file")
            image = request.FILES.get("image")
            if video:
                chapitre.video = video
            if image:
                chapitre.image = image
            chapitre.save()
        except KeyError:
            print("Fichiers non fournis pour le chapitre.")

        chapitre.date_debut = date_debut or chapitre.date_debut
        chapitre.date_fin = date_fin or chapitre.date_fin
        chapitre.save()
        success = True
        message = "Mise à jour effectuée avec succès."
    except school_models.Chapitre.DoesNotExist:
        chapitre = school_models.Chapitre()
        chapitre.titre = title
        chapitre.duree_en_heure = duration
        chapitre.date_debut = date_debut
        chapitre.date_fin = date_fin
        chapitre.description = description
        matiere = school_models.Matiere.objects.get(id=int(matiere))
        chapitre.matiere = matiere
        chapitre.classe = request.user.instructor.classe
        try:
            video = request.FILES.get("file")
            image = request.FILES.get("image")
            if video:
                chapitre.video = video
            if image:
                chapitre.image = image
            chapitre.save()
        except KeyError:
            print("Fichiers non fournis pour le chapitre.")
        success = True
        message = "Chapitre ajouté avec succès."
    except Exception as e:
        print(f"Erreur dans post_cours : {e}")
        success = False
        message = "Une erreur s'est produite."

    data = {
        "success": success,
        "message": message,
        "slug": chapitre.slug if success else "",
    }
    return JsonResponse(data, safe=False)


""" delete chapitre"""


def delete_chapitre(request):
    id = request.POST.get("id")
    try:
        chapitre = school_models.Chapitre.objects.get(id=int(id))
        chapitre.delete()
        success = True
        message = "Le chapitre a bien été supprimé."
    except school_models.Chapitre.DoesNotExist:
        success = False
        message = "Chapitre introuvable."
    except Exception as e:
        print(f"Erreur dans delete_chapitre : {e}")
        success = False
        message = "Une erreur s'est produite."
    data = {
        "success": success,
        "message": message,
    }
    return JsonResponse(data, safe=False)


""" add and update lesson """


def post_lesson(request):
    title = request.POST.get("title")
    chapitre = request.POST.get("chapitre")
    description = request.POST.get("description")
    id = request.POST.get("id")

    try:
        cours = school_models.Cours.objects.get(
            Q(id=int(id)) & Q(chapitre__id=int(chapitre))
        )
        video = request.FILES.get("file")
        image = request.FILES.get("image")
        pdf = request.FILES.get("pdf")
        if video:
            cours.video = video
        if image:
            cours.image = image
        if pdf:
            cours.pdf = pdf
        cours.titre = title
        cours.description = description
        cours.save()
        success = True
        message = "Mise à jour effectuée avec succès."
    except school_models.Cours.DoesNotExist:
        try:
            chapitre_obj = school_models.Chapitre.objects.get(id=int(chapitre))
            cours = school_models.Cours(
                titre=title,
                description=description,
                chapitre=chapitre_obj,
            )
            video = request.FILES.get("file")
            image = request.FILES.get("image")
            pdf = request.FILES.get("pdf")
            if video:
                cours.video = video
            if image:
                cours.image = image
            if pdf:
                cours.pdf = pdf
            cours.save()
            success = True
            message = "Cours ajouté avec succès."
        except Exception as e:
            print(f"Erreur dans post_lesson : {e}")
            success = False
            message = "Une erreur s'est produite."
    except Exception as e:
        print(f"Erreur générale dans post_lesson : {e}")
        success = False
        message = "Une erreur inattendue s'est produite."

    data = {
        "success": success,
        "message": message,
    }
    return JsonResponse(data, safe=False)


""" delete lesson"""


def delete_lesson(request):
    id = request.POST.get("id")
    try:
        lesson = school_models.Cours.objects.get(id=int(id))
        lesson.delete()
        success = True
        message = "La leçon a bien été supprimée."
    except school_models.Cours.DoesNotExist:
        success = False
        message = "Leçon introuvable."
    except Exception as e:
        print(f"Erreur dans delete_lesson : {e}")
        success = False
        message = "Une erreur inattendue s'est produite."

    # Assurez-vous que data est défini dans tous les cas
    data = {
        "success": success,
        "message": message,
    }
    return JsonResponse(data, safe=False)


def update_profil(request):
    nom = request.POST.get("nom")
    prenom = request.POST.get("prenom")
    email = request.POST.get("email")
    bio = request.POST.get("bio")

    try:
        user = User.objects.get(username=request.user.username)
        user.last_name = nom
        user.first_name = prenom
        user.email = email
        user.save()

        instructor = models.Instructor.objects.get(user__id=request.user.id)
        instructor.bio = bio
        instructor.save()

        image = request.FILES.get("file")
        if image:
            instructor.photo = image
            instructor.save()

        success = True
        message = "Vos informations ont été modifiées avec succès."
    except models.Instructor.DoesNotExist:
        success = False
        message = "Instructeur introuvable."
    except Exception as e:
        print(f"Erreur dans update_profil : {e}")
        success = False
        message = "Une erreur s'est produite lors de la mise à jour."
    data = {
        "success": success,
        "message": message,
    }
    return JsonResponse(data, safe=False)


def update_password(request):
    last_password = request.POST.get("last_password")
    new_password = request.POST.get("new_password")
    confirm_password = request.POST.get("confirm_password")

    try:
        if not request.user.check_password(last_password):
            success = False
            message = "Ancien mot de passe incorrect"
        elif new_password != confirm_password:
            success = False
            message = "Les mots de passe ne sont pas identiques"
        else:
            user = User.objects.get(username=request.user.username)
            username = user.username
            user.set_password(new_password)
            user.save()
            user = authenticate(username=username, password=new_password)
            if user:
                login(request, user)
            success = True
            message = "Mot de passe modifié avec succès."
    except Exception as e:
        print(f"Erreur dans update_password : {e}")
        success = False
        message = "Une erreur s'est produite lors de la mise à jour."

    data = {
        "success": success,
        "message": message,
    }
    return JsonResponse(data, safe=False)


"""  Post forum """


def post_forum(request):
    titre = request.POST.get("titre")
    question = request.POST.get("question")
    val = ""
    try:
        forum = forum_models.Sujet()
        forum.titre = titre
        forum.question = question
        forum.user = request.user
        forum.save()
        val = forum.slug
        success = True
        message = "Votre sujet a bien été ajouté!"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la soumission"
    data = {
        "success": success,
        "message": message,
        "forum": val,
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
@login_required(login_url="login")
def save_question(request):
    if request.method == "POST":
        quiz_id = request.POST.get("quiz_id")
        title = request.POST.get("title")
        q_type = request.POST.get("type")
        score = request.POST.get("score")
        answers = request.POST.getlist("answers[]")

        try:
            quiz = quiz_models.Quiz.objects.get(id=quiz_id)

            # Créer ou mettre à jour la question
            question = quiz_models.Question.objects.create(
                quiz=quiz, title=title, question_type=q_type, score=score
            )

            # Ajouter les réponses associées
            for answer in answers:
                quiz_models.Answer.objects.create(question=question, text=answer)

            return JsonResponse(
                {"success": True, "message": "Question saved successfully."}
            )

        except quiz_models.Quiz.DoesNotExist:
            return JsonResponse({"success": False, "message": "Quiz not found."})

    return JsonResponse({"success": False, "message": "Invalid request method."})


@login_required(login_url='login')
def forum_thread_reply(request, slug):
    # Utilisation de get_object_or_404 pour récupérer le sujet en fonction du slug
    forum = get_object_or_404(Sujet, slug=slug)
    if request.method == 'POST':
        # Récupère la réponse depuis le formulaire
        reponse = request.POST.get('comment')
        if reponse and reponse.strip():  # Vérifie si la réponse n'est pas vide
            Reponse.objects.create(
                sujet=forum,  # Associe la réponse au sujet
                user=request.user,
                reponse=reponse
            )
            # Redirige vers le thread
            return redirect('instructor-forum-thread', slug=slug)
        else:
            messages.error(request, "La réponse ne peut pas être vide.")
            return redirect('instructor-forum-thread', slug=slug)
    return redirect('instructor-forum-thread', slug=slug)


@login_required(login_url="login")
def private_chat(request, user_id):
    # Récupère l'utilisateur cible
    other_user = get_object_or_404(User, id=user_id)
    current_user = request.user

    # Contexte pour le template
    context = {
        "other_user": other_user,
        "current_user": current_user,
    }
    return render(request, "pages/private_chat.html", context)
