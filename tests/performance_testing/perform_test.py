
from locust import HttpUser, task, between
from bs4 import BeautifulSoup


class ToDoListUser(HttpUser):
    wait_time = between(5, 10) 

    def on_start(self): 
        self.login() 

   
    def login(self):  
        self.client.post("/login", {
            "username": "User",
            "password": "password"
        })

    @task
    def add_item(self): 
        task_name = "Item Added"
        task_index = 0
        url = f"/newItems?todo_item={task_index}"
        self.client.post(url, data={"todo": task_name})


    @task
    def view_and_verify_list(self):
        # Scenario 3: Bring up entered to-do list and verify accuracy
        response = self.client.get("/list")
        # self.verify_list_accuracy(response)

    @task
    def delete_task_and_review_list(self):
        # Scenario 4: Delete item and review list again to ensure it is not there
        # Add a task first for deletion
        task_name = "Task to Delete"
        task_index = 0  # Adjust the task index as needed
        url = f"/deleteItems?todo_item={task_index}"
        self.client.post(url, data={"todo": task_name})

        # Get the current list
        initial_list_response = self.client.get("/list")

        
        # Verify the task is removed
        updated_list_response = self.client.get("/list")

        self.verify_list_accuracy(updated_list_response, True)


    def login(self):
        username = "User"
        password = "password"
        self.client.post("/", data={"username": username, "password": password})

    def verify_list_accuracy(self, response, task_deleted=False):
        html_content = response.text 
        soup = BeautifulSoup(html_content, 'html.parser')

        print(f"RESPONSE  TEST : {response.text}")
        if task_deleted:
            assert "Task to Delete" not in soup.get_text()
        else:
            assert "New Task 1" in soup.get_text()
