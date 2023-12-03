# Charne Robinson
# December 1st, 2023
# Performance Testing - Scenario 2


from locust import HttpLocust, TaskSet, task, between


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        self.client.post("/login", {
            "username": "User",
            "password": "password"
        })

    @task
    def add_item(self):
        add_item = "Tomato"
    # I didn't know what else to put here :(


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 10)
