from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from school import models as school_models
from forum import models as forum_models
from instructor import models as instructor_models
from django.db.models import Q
from chat import models as chat_models
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import authenticate, login
from school.models import Cours


# Create your views here.
@login_required(login_url="guest-login")
def index(request):
    try:
        if hasattr(request.user, "instructor"):
            return redirect("instructor-dashboard")
        elif hasattr(request.user, "student_user"):
            cours = Cours.objects.filter(
                Q(status=True) & Q(chapitre__classe=request.user.student_user.classe)
            ).order_by("-date_add")[:5]
            forum = forum_models.Sujet.objects.filter(
                cours__chapitre__classe=request.user.student_user.classe
            )[:5]
            forum_count = forum_models.Sujet.objects.filter(
                cours__chapitre__classe=request.user.student_user.classe
            ).count()
            datas = {"cours": cours, "forum": forum, "forum_count": forum_count}
            return render(request, "pages/fixed-student-dashboard.html", datas)
        else:
            return redirect("guest-login")
    except Exception as e:
        print(f"Error in index view: {e}")
        return HttpResponse("Une erreur est survenue : {}".format(e), status=500)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if hasattr(user, "instructor"):
                return redirect("dashboard")
            elif hasattr(user, "student_user"):
                return redirect("index_student")
            else:
                return render(
                    request,
                    "pages/guest-login.html",
                    {"error": "Aucun rôle associé à cet utilisateur."},
                )
        else:
            return render(
                request, "pages/guest-login.html", {"error": "Identifiants incorrects."}
            )

    return render(request, "pages/guest-login.html")


@login_required(login_url="login")
def payment(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(
                    request,
                    "pages/fixed-student-account-billing-payment-information.html",
                    datas,
                )
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def subscription(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(
                    request,
                    "pages/fixed-student-account-billing-subscription.html",
                    datas,
                )
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def upgrade(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(
                    request, "pages/fixed-student-account-billing-upgrade.html", datas
                )
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def edit(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-account-edit.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def edit_basic(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(
                    request, "pages/fixed-student-account-edit-basic.html", datas
                )
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def edit_profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(
                    request, "pages/fixed-student-account-edit-profile.html", datas
                )
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def billing(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-billing.html", datas)
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
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     cours = school_models.Cours.objects.filter(Q(status=True) &
#                     Q(chapitre__classe=request.user.student_user.classe))
#                     datas = {
#                                 'all_cours' : all_cours ,
#                            }
#                 return render(request,'pages/fixed-student-browse-courses.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def cart(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-cart.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-courses.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


# @login_required(login_url = 'login')
# def dashboard(request):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     datas = {

#                            }
#                 return render(request,'pages/fixed-student-dashboard.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def earnings(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-earnings.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def forum(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    forum_general = forum_models.Sujet.objects.filter(cours=None)
                    forum = forum_models.Sujet.objects.filter(
                        cours__chapitre__classe=request.user.student_user.classe
                    )
                    datas = {
                        "forum_general": forum_general,
                        "forum": forum,
                    }
                return render(request, "pages/fixed-student-forum.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def forum_lesson(request, slug):
    try:
        if hasattr(
            request.user, "student_user"
        ):  # Vérifie que l'utilisateur est un étudiant
            lesson = school_models.Cours.objects.get(slug=slug)
            # Récupère les forums associés à la leçon
            forums = forum_models.Sujet.objects.filter(cours=lesson)
            datas = {
                "lesson": lesson,
                "forums": forums,
            }
            return render(request, "pages/fixed-student-forum-lesson.html", datas)
        else:
            return redirect("dashboard")  # Redirige les instructeurs
    except Exception as e:
        print(f"Erreur dans forum_lesson: {e}")
        return redirect("forum")  # Redirige en cas d'erreur


@login_required(login_url="login")
def forum_ask(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-forum-ask.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def forum_thread(request, slug):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    forum = forum_models.Sujet.objects.get(slug=slug)
                    datas = {
                        "forum": forum,
                    }
                return render(request, "pages/fixed-student-forum-thread.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def help_center(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-help-center.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def invoice(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-invoice.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def messages(request, classe):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    exist_classe = chat_models.Salon.objects.get(
                        classe=request.user.student_user.classe
                    )
                    info = school_models.Classe.objects.get(
                        id=request.user.student_user.classe.id
                    )
                    instructor = instructor_models.Instructor.objects.get(
                        classe__id=request.user.student_user.classe.id
                    )
                    user_room = ""
                    print(user_room)
                    datas = {
                        "instructor": instructor,
                        "info_classe": info,
                        "classe": exist_classe,
                        "classe_json": mark_safe(json.dumps(exist_classe.id)),
                        "username": mark_safe(json.dumps(request.user.username)),
                    }
                return render(request, "pages/fixed-student-messages.html", datas)
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
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     datas = {

#                            }
#                 return render(request,'pages/fixed-student-messages-2.html',datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def my_courses(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    chapitre = school_models.Chapitre.objects.filter(status=True)
                    cours = school_models.Cours.objects.filter(status=True)
                    all_cours = school_models.Cours.objects.filter(
                        Q(status=True)
                        & Q(chapitre__classe=request.user.student_user.classe)
                    )
                    datas = {
                        "chapitre": chapitre,
                        "cours": cours,
                        "all_cours": all_cours,
                    }
                return render(request, "pages/fixed-student-my-courses.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def quiz_list(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-quiz-list.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def profile(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-profile.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def profile_posts(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-profile-posts.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="guest-login")
def quiz_results(request):
    if hasattr(
        request.user, "student_user"
    ):  # Vérifie si l'utilisateur est un étudiant
        try:
            # Simulez des résultats pour les quizzes.
            quizzes = [
                {
                    "title": "Basics of HTML",
                    "course": "HTML Course",
                    "score": 5.8,
                    "status": "Good",
                },
                {
                    "title": "Directives & Routing",
                    "course": "Angular in Steps",
                    "score": 9.8,
                    "status": "Great",
                },
                {
                    "title": "Responsive & Retina",
                    "course": "Bootstrap Foundations",
                    "score": 2.8,
                    "status": "Failed",
                },
            ]

            datas = {
                "quizzes": quizzes,
            }
            return render(request, "pages/fixed-student-quiz-results.html", datas)
        except Exception as e:
            print(f"Error in quiz_results view: {e}")
            return HttpResponse("Une erreur est survenue : {}".format(e), status=500)
    else:
        return redirect("dashboard")  # Redirige si l'utilisateur n'est pas un étudiant


@login_required(login_url="login")
def quizzes(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-quizzes.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="login")
def statement(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-statement.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


# @login_required(login_url = 'login')
# def student_take_course(request, slug):
#     if request.user.is_authenticated:
#         try:
#             try:
#                 print("1")
#                 if request.user.instructor:
#                     return redirect('dashboard')
#             except Exception as e:
#                 print(e)
#                 print("2")
#                 if request.user.student_user:
#                     cours  = school_models.Cours.objets.get(slug=slug)
#                     datas = {
#                         'cours': cours,
#                     }
#                 return render(
#                       request,'pages/fixed-student-student-take-course.html',
#                       datas)
#         except Exception as e:
#             print(e)
#             print("3")
#             return redirect("/admin/")


@login_required(login_url="login")
def take_course(request, slug):
    if request.user.is_authenticated:
        try:
            # Si l'utilisateur est un instructeur, redirection vers le tableau de bord
            if hasattr(request.user, "instructor"):
                return redirect("dashboard")

            # Si l'utilisateur est un étudiant, charger le cours
            if hasattr(request.user, "student_user"):
                try:
                    cours = school_models.Cours.objects.get(slug=slug)
                    instructor = instructor_models.Instructor.objects.get(
                        classe=request.user.student_user.classe
                    )
                    datas = {
                        "cours": cours,
                        "instructor": instructor,
                    }
                    return render(
                        request, "pages/fixed-student-take-course.html", datas
                    )
                except school_models.Cours.DoesNotExist:
                    return HttpResponse("Cours introuvable", status=404)
                except instructor_models.Instructor.DoesNotExist:
                    return HttpResponse("Instructeur introuvable", status=404)

        # Gestion des erreurs inattendues
        except Exception as e:
            print(f"Erreur inattendue dans take_course : {e}")
            return HttpResponse("Une erreur est survenue.", status=500)

    # Si l'utilisateur n'est pas authentifié
    return redirect("login")


@login_required(login_url="guest-login")
def take_quiz(request):
    try:
        if hasattr(request.user, "instructor"):
            return redirect("dashboard")  # Redirige les instructeurs

        if hasattr(
            request.user, "student_user"
        ):  # Vérifie si l'utilisateur est un étudiant
            # Simulez des données fictives pour l'exemple
            datas = {
                "quiz_title": "Sample Quiz",
                "questions": [
                    {"id": 1, "text": "What is Django?", "status": "Correct"},
                    {"id": 2, "text": "Define MVC.", "status": "Wrong"},
                ],
            }
            return render(request, "pages/fixed-student-take-quiz.html", datas)

        return redirect("guest-login")
    except Exception as e:
        print(f"Error in take_quiz: {e}")
        return HttpResponse("Une erreur est survenue : {}".format(e), status=500)


@login_required(login_url="login")
def view_course(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.instructor:
                    return redirect("dashboard")
            except Exception as e:
                print(e)
                print("2")
                if request.user.student_user:
                    datas = {}
                return render(request, "pages/fixed-student-view-course.html", datas)
        except Exception as e:
            print(e)
            print("3")
            return redirect("/admin/")


@login_required(login_url="guest-login")
def account_edit(request):
    if hasattr(request.user, "instructor"):
        datas = {"message": "Modifier les informations du professeur."}
        return render(request, "pages/instructor-account-edit.html", datas)
    elif hasattr(request.user, "student_user"):
        datas = {"message": "Modifier les informations de l'étudiant."}
        return render(request, "pages/fixed-student-account-edit.html", datas)
    return redirect("guest-login")


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
        student = models.Student.objects.get(user__id=request.user.id)
        student.bio = bio
        student.save()

        try:
            image = request.FILES["file"]
            student.photo = image
            student.save()
        except KeyError:  # Exception spécifiée pour l'absence de fichier
            pass

        success = True
        message = "Vos informations ont été modifiées avec succès."
    except models.Student.DoesNotExist:  # Spécifiez si l'étudiant n'existe pas
        success = False
        message = "L'étudiant n'existe pas."
    except Exception as e:  # Capture d'autres exceptions pour les journaliser
        success = False
        message = f"Une erreur est survenue lors de la mise à jour : {str(e)}"

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
            user.password = new_password
            user.set_password(user.password)
            user.save()
            user = authenticate(username=username, password=new_password)
            login(request, user)
            success = True
            message = "Mot de passe modfifié avec succès"
    except Exception as e:
        print(e)
        success = False
        message = "une erreur est subvenue lors de la mise à jour"
    data = {
        "success": success,
        "message": message,
    }
    return JsonResponse(data, safe=False)


def post_forum(request):
    titre = request.POST.get("titre")
    question = request.POST.get("question")
    val = ""
    try:
        if not titre or not question:
            raise ValueError("Titre et question sont obligatoires.")

        forum = forum_models.Sujet()
        forum.titre = titre
        forum.question = question
        forum.user = request.user
        forum.save()  # Le slug unique sera généré dans le modèle
        val = forum.slug
        success = True
        message = "Votre sujet a bien été ajouté!"
    except ValueError as ve:
        success = False
        message = str(ve)
    except Exception as e:
        print(e)
        success = False
        message = "Une erreur est survenue lors de la soumission."
    data = {
        "success": success,
        "message": message,
        "forum": val,
    }
    return JsonResponse(data, safe=False)


def post_forum_g(request):
    if request.method == "POST":
        titre = request.POST.get("titre")
        question = request.POST.get("question")
        val = ""
        try:
            # Vérification des champs obligatoires
            if not titre or not question:
                return JsonResponse(
                    {"success": False, "message": "Tous les champs sont obligatoires."},
                    safe=False,
                )

            # Création du sujet dans le forum général
            forum = forum_models.Sujet.objects.create(
                titre=titre, question=question, user=request.user
            )
            val = forum.slug
            return JsonResponse(
                {
                    "success": True,
                    "message": "Votre sujet a bien été ajouté!",
                    "forum": val,
                },
                safe=False,
            )
        except Exception as e:
            print(f"Erreur lors de la soumission : {e}")
            return JsonResponse(
                {
                    "success": False,
                    "message": "Une erreur est survenue lors de la soumission.",
                },
                safe=False,
            )

    return JsonResponse(
        {"success": False, "message": "Méthode non autorisée."}, safe=False
    )


@login_required(login_url="login")
def post_response(request, slug):
    if request.method == "POST":
        try:
            forum = forum_models.Sujet.objects.get(slug=slug)
            reponse_text = request.POST.get("reponse")

            if reponse_text.strip():  # Vérifie que le champ n'est pas vide
                reponse = forum_models.Reponse.objects.create(
                    user=request.user, sujet=forum, reponse=reponse_text
                )
                reponse.save()
                return redirect("forum-thread", slug=slug)
            else:
                return redirect("forum-thread", slug=slug)  # Pas de réponse vide
        except forum_models.Sujet.DoesNotExist:
            return redirect("forum")  # Forum introuvable
        except Exception as e:
            print(f"Erreur dans post_response: {e}")
            return redirect("forum")  # Redirection générique en cas d'erreur
