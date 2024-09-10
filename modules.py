import json
import os
from datetime import datetime

#Function for entry inputs for to do a action.
def validate_action():
        print("""Type the number that you need:
                            1.Add Tasks.
                            2.Update Tasks.
                            3.Delete Tasks.
                            4.Mark a task as in progress.
                            5.Mark a task as done.
                            6.Show all tasks.
                            7.Show all tasks that are done.
                            8.Show all tasks that are not done.
                            9.Show all tasks that are in progress.
                            0.Close app.
                       """)
        action = int(input())
        actions = 1,2,3,4,5,6,7,8,9,0
        while not action in actions:
            print(f"{action} is invalid.")
            action = input()
        return action

#Create the storage for the tasks.
def create_file_json():
    json_path = 'tasks.json'
    #Create a json if not exist yet.
    if not os.path.exists(json_path):
        with open(json_path, 'w') as json_file:
            json.dump({"tasks": {}}, json_file, indent=4)

#Function for create and add the task in tasks.json.    
def add_task(new_task):
        json_path = 'tasks.json'
        
        #Read the json file.
        with open(json_path, 'r') as json_file:
            data = json.load(json_file) #Try load json file.

        #Add a new task. 
        data["tasks"].update(new_task)

        with open(json_path, 'r+') as json_file:
            #Overrite at the beginning of the file.
            json.dump(data, json_file, indent=4)

        return "A new task was created."

#Validate and create unique id
def unique_id():
    id_counter = 0
    id_counter +=1
    id_task = id_counter
    id_repeated = []

    json_path = 'tasks.json'
    try:
        with open(json_path, 'r') as json_file:
                data = json.load(json_file) #Try load json file.
                for n in data["tasks"]:
                    id_repeated.append(int(n))
                while id_task in id_repeated:
                    id_task += 1
                else:
                    values = {"id": str(id_task), "id_list": id_repeated}
                    return values
    except:
         return {"id": str(id_task)}
        

#Validate that the description has content.
def validate_description():
        description = input("Please type the task: ")
        while not description.strip():  #Make sure is not empty.
            print("Task cannot be empty. Please enter a valid description.")
            description = input("Please type the task again: ")
        return description

#Function to update the tasks and validate that tasks.json has added tasks.
def update_task(id_list):
    if not len(id_list) == 0:
        id_task = int(input("Type the id of the task to update: "))
        while not id_task in id_list:
            id_task = int(input(f"Task with id: {id_task} doesn't exist. Type again the id of the task to update: "))
        else:
            description = validate_description()
            time = datetime.now()
            updatedAt = time.strftime('%Y-%m-%d %H:%M:%S')
            
            json_path = 'tasks.json'
            with open(json_path, 'r') as json_file:
                add_update = json.load(json_file)
                
            add_update["tasks"][str(id_task)]["Description"] = description
            add_update["tasks"][str(id_task)]["Updated_at"] = updatedAt
            with open(json_path, 'w') as json_file:
                json.dump(add_update, json_file, indent=4)
            
        return f"The task {id_task} was updated succesfully"
    else:
         return "You need to add tasks first to update them"

#Delete tasks in tasks.json and validate that tasks.json has added tasks.
def delete_task(id_list):
    id_task = int(input("Type the id of the task to delete: "))
    if not len(id_list) == 0:
        while not id_task in id_list:
            id_task = int(input(f"Task with id: {id_task} doesn't exist. Type again the id of the task to delete: "))
        else:
            json_path = 'tasks.json'
            with open(json_path, 'r') as json_file:
                data_task = json.load(json_file)
            del data_task["tasks"][str(id_task)]
            with open(json_path, 'w') as json_file:
                json.dump(data_task, json_file, indent=4)
            
        return f"The task with id: {id_task} was deleted succesfully"
    else:
         return "There are not tasks here"

#Function to update the status of a task by its ID.
def status(id_list, option):
    if not len(id_list) == 0:
        id_task = int(input("Type the id of the task to update the status: "))
        while not id_task in id_list:
            id_task = int(input(f"Task with id: {id_task} doesn't exist. Type again the id of the task to update the status: "))
        else:
            status = {"in-p":"in-progress", "done": "done"}
            time = datetime.now()
            updatedAt = time.strftime('%Y-%m-%d %H:%M:%S')
            
            
            json_path = 'tasks.json'
            with open(json_path, 'r') as json_file:
                add_update = json.load(json_file)
            
            if option == 4:
                add_update["tasks"][str(id_task)]["Status"] = status["in-p"]
                msg = print(f"The task {id_task} is {status['in-p']}")
            else:
                add_update["tasks"][str(id_task)]["Status"] = status["done"]
                msg = print(f"The task {id_task} is {status["done"]}")

            add_update["tasks"][str(id_task)]["Updated_at"] = updatedAt
            with open(json_path, 'w') as json_file:
                json.dump(add_update, json_file, indent=4)
            
        return msg
    else:
         return "You need to add tasks first to update them"

#Validate if there are tasks and display all tasks.
def show_all_tasks():
    json_path = 'tasks.json'
    with open(json_path, 'r') as json_file:
        data_tasks = json.load(json_file)
    if data_tasks["tasks"] == {}:
        return "There are not tasks"
    else:  
        return data_tasks 

#Find tasks with status == 'done' and display them.
def show_tasks_done():
    tasks_id_done = []
    data_tasks = show_all_tasks()
    for id_task in data_tasks["tasks"]:
        if data_tasks["tasks"][id_task]["Status"] == "done":
            tasks_id_done.extend([id_task, data_tasks["tasks"][id_task]])
    
    if len(tasks_id_done) == 0:
        return "There are not tasks done"
    else:
        return tasks_id_done

#Find tasks with status == 'to-do' or 'in-progress' and display them.
def show_tasks_not_done():
    tasks_not_done = []
    data_tasks = show_all_tasks()
    for id_task in data_tasks["tasks"]:
        if not data_tasks["tasks"][id_task]["Status"] == "done":
            tasks_not_done.extend([id_task, data_tasks["tasks"][id_task]])
    
    if len(tasks_not_done) == 0:
        return "The tasks probably done or there are not tasks."
    else:
        return tasks_not_done

#Find tasks with status == 'in-progress' and display them.
def show_tasks_in_progress():
    tasks_id_progress = []
    data_tasks = show_all_tasks()
    for id_task in data_tasks["tasks"]:
        if data_tasks["tasks"][id_task]["Status"] == "in-progress":
            tasks_id_progress.extend([id_task, data_tasks["tasks"][id_task]])
    
    if len(tasks_id_progress) == 0:
        return "There are not tasks in-progress"
    else:
        return tasks_id_progress
