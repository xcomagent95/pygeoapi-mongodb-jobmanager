from locust import HttpUser, task
import random
from urllib.request import urlopen
import json
class pygeoapiPerformanceTest(HttpUser):
    @task
    def jobs(self):

        host = self.client.base_url

        status = ["accepted", "running", "successful", "failed", "dismissed"]

        responseJobs = urlopen(host + 'jobs?f=json')
        stringJobs = responseJobs.read().decode('utf-8')
        jsonJobs = json.loads(stringJobs)
        jobIDs = []
        completedJobs = []
        for i in jsonJobs["jobs"]:
            jobIDs.append(i["jobID"])
            if i['status'] == 'successful':
                completedJobs.append(i["jobID"])

        responseCollections = urlopen(host + 'collections?f=json')
        string = responseCollections.read().decode('utf-8')
        jsonCollections = json.loads(string)
        collections = []
        for i in jsonCollections["collections"]:
            name = i["id"]
            responseItems = urlopen(host + 'collections/' + name +'/items?f=json')
            stringItems = responseItems.read().decode('utf-8')
            jsonItems = json.loads(stringItems)
            items = []
            for y in jsonItems["features"]:
                items.append(y["properties"]["id"])
            collections.append((name, items))

        #get main page 
        self.client.get(host)
        #get conformance
        self.client.get("/conformance?")
        #get api def
        self.client.get("/openapi?f=json")
        #get collections
        self.client.get("/collections/portolan")
        #get collections
        self.client.get("/collections?")
        #get collection
        self.client.get("/collections/" + random.choice(collections)[0])
        #get items
        self.client.get("/collections/" + random.choice(collections)[0] + "/items")
        #get items
        collection = random.choice(collections)
        self.client.get("/collections/" + collection[0] + "/items/" + str(random.choice(collection[1])))
        #get processes
        self.client.get("/processes")
        #get jobs
        self.client.get("/jobs?f=json")
        #get jobs with status
        self.client.get("/jobs?status=" + random.choice(status))
        #get job
        self.client.get("/jobs/" + random.choice(jobIDs))
        #get results 
        self.client.get("/jobs/" + random.choice(completedJobs) + "/results")   
