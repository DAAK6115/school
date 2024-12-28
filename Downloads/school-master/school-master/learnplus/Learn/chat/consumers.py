# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

# from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Salon, Message
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        # messages = Message.last_10_messages()
        salon = data["classe"]
        messages = (
            Message.objects.filter(salon__classe=int(salon))
            .order_by("date_add")
            .all()[:20]
        )
        content = {"command": "messages", "messages": self.messages_to_json(messages)}
        self.send_message(content)

    def new_message(self, data):
        auteur = data["from"]
        salon = data["classe"]
        salon_object = Salon.objects.get(classe__id=int(salon))
        auteur_user = User.objects.filter(username=auteur)[0]
        message = Message.objects.create(
            auteur=auteur_user, salon=salon_object, message=data["message"]
        )
        content = {"command": "new_message", "message": self.message_to_json(message)}
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        print(messages)
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        try:
            image = message.auteur.student_user.photo.url
        except AttributeError:
            try:
                image = message.auteur.instructor.photo.url
            except AttributeError:
                image = None  # Image par défaut ou gestion d'absence d'image

                return {
                    "auteur": message.auteur.username,
                    "auteur_image": image,
                    "message": message.message,
                    "date_add": str(message.date_add.year)
                    + "-"
                    + str(message.date_add.month)
                    + "-"
                    + str(message.date_add.day)
                    + " "
                    + str(message.date_add.hour)
                    + ":"
                    + str(message.date_add.minute)
                    + ":"
                    + str(message.date_add.second),
                }

    commands = {
        "fetch_messages": fetch_messages,
        "new_message": new_message,
    }
    # async def connect(self):

    def connect(self):
        self.salon = self.scope["url_route"]["kwargs"]["classe"]
        self.room_group_name = "chat_%s" % self.salon

        # Join room group
        # await self.channel_layer.group_add(
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data["command"]](self, data)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group

    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))


class PrivateChatConsumer(WebsocketConsumer):
    def connect(self):
        self.other_user_id = int(
            self.scope["url_route"]["kwargs"]["user_id"]
        )  # Convertit en entier

        # Construction de la room_name
        self.room_name = (
            f'private_chat_'
            f'{min(self.scope["user"].id, self.other_user_id)}_'
            f'{max(self.scope["user"].id, self.other_user_id)}'
        )

        # Ajouter l'utilisateur au groupe
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # Retirer l'utilisateur du groupe
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.channel_name
        )

    def receive(self, text_data):
        # Traiter les données reçues
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = self.scope["user"].username

        # Envoyer le message au groupe
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender,
            },
        )

    def chat_message(self, event):
        # Recevoir le message du groupe
        self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                    "sender": event["sender"],
                }
            )
        )
