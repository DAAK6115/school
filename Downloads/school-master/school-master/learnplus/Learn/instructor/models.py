from django.db import models
from django.contrib.auth.models import User
from school import models as school_models
from django.utils.text import slugify


# Create your models here.
class Instructor(models.Model):
    user = models.OneToOneField(
        User, related_name="instructor", on_delete=models.CASCADE
    )
    contact = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    classe = models.ForeignKey(
        school_models.Classe,
        related_name="instructor_classe",
        on_delete=models.CASCADE,
        null=True,
    )
    photo = models.ImageField(upload_to="images/Instructor", default="github.png")
    bio = models.TextField(default="Votre bio")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Instructor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

    def __str__(self):
        return self.user.username

    @property
    def get_u_type(self):
        try:
            return True
        except Exception as e:
            print(f"Erreur dans get_u_type : {e}")
        return False


class ForumQuestion(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    topic = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Forum(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Génère un slug seulement si le champ est vide
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)


class ForumReponse(models.Model):
    forum = models.ForeignKey(
        Forum, related_name="sujet_reponse", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reponse = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réponse de {self.user} sur {self.forum.titre}"


class PrivateMessage(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"
