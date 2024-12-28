from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_request, logout
from django.shortcuts import redirect
import json
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        try:
            if hasattr(request.user, "student_user"):
                return redirect("index_student")
            elif hasattr(request.user, "instructor"):
                return redirect("dashboard")
        except Exception as e:
            print(f"Erreur dans login : {e}")
            return redirect("/admin/")
    else:
        datas = {}
        return render(request, "pages/guest-login.html", datas)


def signup(request):
    if request.user.is_authenticated:
        try:
            if hasattr(request.user, "student_user"):
                return redirect("index_student")
            elif hasattr(request.user, "instructor"):
                return redirect("dashboard")
        except Exception as e:
            print(f"Erreur dans signup : {e}")
            return redirect("/admin/")
    else:
        datas = {}
        return render(request, "pages/guest-signup.html", datas)


def forgot_password(request):
    if request.user.is_authenticated:
        try:
            if hasattr(request.user, "student_user"):
                return redirect("index_student")
            elif hasattr(request.user, "instructor"):
                return redirect("dashboard")
        except Exception as e:
            print(f"Erreur dans forgot_password : {e}")
            return redirect("/admin/")
    else:
        datas = {}
        return render(request, "pages/guest-forgot-password.html", datas)


def islogin(request):
    postdata = json.loads(request.body.decode("utf-8"))
    username = postdata["username"]
    password = postdata["password"]
    u_type = ""

    try:
        # Authentification par email ou username
        user = None
        if "@" in username:
            user = authenticate(email=username, password=password)
            utilisateur = User.objects.get(email=username)
        else:
            user = authenticate(username=username, password=password)
            utilisateur = User.objects.get(username=username)

        # Vérification des informations d'authentification
        if user and user.is_active:
            login_request(request, user)
            if hasattr(utilisateur, "student_user"):
                u_type = "student"
            elif hasattr(utilisateur, "instructor"):
                u_type = "instructor"
            else:
                u_type = "admin"

            return JsonResponse(
                {
                    "redirect": u_type,
                    "success": True,
                    "message": "Vous êtes connectés!!!",
                },
                safe=False,
            )

        # Identifiants incorrects
        return JsonResponse(
            {"success": False, "message": "Vos identifiants ne sont pas corrects"},
            safe=False,
        )

    except Exception as e:
        print(f"Erreur dans islogin : {e}")
        return JsonResponse(
            {"success": False, "message": "Une erreur s'est produite"}, safe=False
        )


def deconnexion(request):
    logout(request)
    return redirect("login")
