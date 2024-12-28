from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    @task
    def load_homepage(self):
        # Assurez-vous que la route "/" existe dans votre application.
        self.client.get("/")

    @task
    def submit_form(self):
        # Remplacez "/form-submit"
        # par le chemin réel de votre endpoint.

        self.client.post(
            "/instructor/forum_thread/test-86149/reply/",
            data={"name": "test", "email": "test@example.com"})


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
