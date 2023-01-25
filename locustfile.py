from locust import HttpUser, task
import random

ids = ['74dc0f05-8dbf-11ed-8434-54e1ad4efa81',
       'c00786e2-98be-11ed-8f20-54e1ad4efa81',
       '23cf474b-98c3-11ed-9f17-54e1ad4efa81',
       '36ca8d2c-98c3-11ed-b1fc-54e1ad4efa81',
       'd1298c54-98c3-11ed-a6ef-54e1ad4efa81',
       'e7b255a9-98c3-11ed-b1cc-54e1ad4efa81']

status = ["accepted", "running", "successful", "failed", "dismissed"]

class HelloWorldUser(HttpUser):
    @task
    def jobs(self):
        #get jobs
        self.client.get("http://localhost:5000/jobs?f=json")
        #get jobs with status
        self.client.get("http://localhost:5000/jobs?status=" + random.choice(status) + "&f=json")
        #get job
        self.client.get("http://localhost:5000/jobs/" + random.choice(ids) + "?f=json")
        #get results 
        self.client.get("http://localhost:5000/jobs/" + random.choice(ids) + "/results?f=json")
        