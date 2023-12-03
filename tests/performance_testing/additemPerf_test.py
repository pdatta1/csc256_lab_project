# Charne Robinson
# December 1st, 2023
# Performance Testing - Scenario 2


from locust import HttpUser, TaskSet, task, between


class UserBehavior(HttpUser):
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
        # Scenario 2: Add item to the to-do list
        task_name = "Item added"
        task_index = 0  
        url = f"/newItems?todo_item={task_index}"
        self.client.post(url, data={"todo": task_name})


class WebsiteUser(HttpUser):
    task_set = UserBehavior
    wait_time = between(5, 10)
