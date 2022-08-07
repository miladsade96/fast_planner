from locust import HttpUser, task, between
from planner.models.users import UserSignIn



class WebsiteUser(HttpUser):
    wait_time = between(0.5, 3.0)
    user_signin = UserSignIn(email="test@test.com", password="test")

    def on_start(self):
        self.client.post("/user/signin", WebsiteUser.user_signin)


    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/event/")
