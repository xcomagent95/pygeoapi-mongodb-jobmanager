from locust import HttpUser, task
import random
from urllib.request import urlopen
import json
class pygeoapiPerformanceTest(HttpUser):
    @task
    def jobs(self):

        status = ["accepted", "running", "successful", "failed", "dismissed"]

        response = urlopen('http://localhost:5000/jobs?f=json')
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        jobIDs = []
        completedJobs = []
        for i in json_obj["jobs"]:
            jobIDs.append(i["jobID"])
            if i['status'] == 'successful':
                completedJobs.append(i["jobID"])

        #add collections and items
        #start processes from here

        #get main page 
        self.client.get("http://localhost:5000/")
        #get conformance
        self.client.get("http://localhost:5000/conformance?f=html")
        #get api def
        self.client.get("http://localhost:5000/openapi?f=json")
        #get collections
        self.client.get("http://localhost:5000/collections/portolan")
        #get collection
        self.client.get("http://localhost:5000/collections?f=html")
        #get items
        self.client.get("http://localhost:5000/collections/portolan/items")
        #get jobs
        self.client.get("http://localhost:5000/jobs?f=json")
        #get jobs with status
        self.client.get("http://localhost:5000/jobs?status=" + random.choice(status) + "&f=json")
        #get job
        self.client.get("http://localhost:5000/jobs/" + random.choice(jobIDs) + "?f=json")
        #get results 
        #Fehler kommen durch einen Fehler in der pygeoAPI zustande. Hier wird 400 anstatt 200 zurückgegeben wenn ein Job Fehlegschlagen ist
        self.client.get("http://localhost:5000/jobs/" + random.choice(completedJobs) + "/results?f=json")   

