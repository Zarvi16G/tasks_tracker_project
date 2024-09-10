from modules import *
from datetime import datetime

#We use an instance of the Task class to form the body of a task.
class Task:
    def __init__(self, id_task, description, status):
        self.id_task = id_task
        self.description = description
        self.status = status
        time = datetime.now()
        self.createdAt = time.strftime('%Y-%m-%d %H:%M:%S')

    #Then we return all the task data as a dict.
    def as_dict(self):
        task = {
            self.id_task: {
                    "Description": self.description,
                    "Status": self.status,
                    "Created_at": self.createdAt,
                    }   
                }   
        return task
    