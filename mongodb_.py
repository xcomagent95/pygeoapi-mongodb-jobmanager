#MongoDB Job-Manager
from pygeoapi.process.manager.base import BaseManager
from pygeoapi.util import JobStatus
from pymongo import MongoClient
import traceback
import json

class MongoDBManager(BaseManager):
    def __init__(self, manager_def):
        super().__init__(manager_def)
        self.is_async = True

    def _connect(self):
        #connection in CFG would be something like mongodb://localhost:27017/
        try:
            client = MongoClient(self.connection)
            self.db = client
            print("JOBMANAGER - MongoDB connected")
            return True
        except:
            self.destroy()
            print("JOBMANAGER - connect error")
            traceback.print_exc()
            return False

    def destroy(self):
        try:
            self.db.close()
            print("JOBMANAGER - MongoDB disconnected")
            return True
        except:
            self.destroy()
            print("JOBMANAGER - destroy error")
            traceback.print_exc()
            return False

    def get_jobs(self, status=None):
        try:
            self._connect()
            database = self.db.job_manager_pygeoapi
            collection = database.jobs
            jobs = list(collection.find({}))
            print("JOBMANAGER - MongoDB jobs queried")
            self.destroy()
            return jobs
        except:
            self.destroy()
            print("JOBMANAGER - get_jobs error")
            traceback.print_exc()
            return False

    def add_job(self, job_metadata):
        try:
            self._connect()
            database = self.db.job_manager_pygeoapi
            collection = database.jobs

            doc_id = collection.insert_one(job_metadata)

            self.db.close()
            print("JOBMANAGER - MongoDB job added")
            self.destroy()
            return doc_id
        except:
            self.destroy()
            print("JOBMANAGER - add_job error")
            traceback.print_exc()
            return False

    def update_job(self, job_id, update_dict):
        try:            
            self._connect()
            database = self.db.job_manager_pygeoapi
            collection = database.jobs
            entry = collection.find_one( {"identifier" : job_id})
            print(entry)
            print(update_dict)
            collection.update_one(entry, {"$set": update_dict})
            print("JOBMANAGER - MongoDB job updated")
            self.destroy()
            return True
        except:
            self.destroy()
            print("JOBMANAGER - MongoDB update_job error")
            traceback.print_exc()
            return False

    def delete_job(self, job_id):
        try:
            self._connect()
            database = self.db.job_manager_pygeoapi
            collection = database.jobs
            collection.delete_one({"identifier": job_id})
            print("JOBMANAGER - MongoDB job deleted")
            self.destroy()
            return True
        except:
            self.destroy()
            print("JOBMANAGER - MongoDB delete_job error")
            traceback.print_exc()
            return False

    def get_job(self, job_id):
        try:
            self._connect()
            database = self.db.job_manager_pygeoapi
            collection = database.jobs
            entry = collection.find_one( {"identifier" : job_id})
            print("JOBMANAGER - MongoDB job queried")
            self.destroy()
            return entry
        except:
            self.destroy()
            print("JOBMANAGER - MongoDB get_job error")
            traceback.print_exc()
            return False

    def get_job_result(self, job_id):
        try:
            self._connect()
            database = self.db.job_manager_pygeoapi
            collection = database.jobs
            entry = collection.find_one( {"identifier" : job_id})
            if entry["status"] != "successful":
                print("JOBMANAGER - job not finished or failed")
                return (None,)
            with open(entry["location"], "r") as file:
                data = json.load(file)
            self.destroy()
            print("JOBMANAGER - MongoDB job result queried")
            return entry["mimetype"], data
        except:
            self.destroy()
            print("JOBMANAGER - MongoDB get_job_result error")
            traceback.print_exc()
            return False

    def __repr__(self):
        return '<MongoDBManager> {}'.format(self.name)
