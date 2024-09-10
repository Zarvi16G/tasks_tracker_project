from classes import *
from art import *
from modules import *
import pprint

def main():
    #Print initial design.
    art_design = art
    print(art_design)

    #Validate if tasks.json exist.
    create_file_json()


    while True:
        #Validate user values
        option_user = validate_action()

        #Option 1 == add tasks.
        if option_user == 1:
            description_task = validate_description()
            id_task = unique_id()
            task = Task(id_task["id"], description_task, status="to-do")
            data_task = task.as_dict()
            new_task = add_task(data_task)
            print(new_task)

        #Option 2 == update tasks.
        elif option_user == 2:
            id_list = unique_id()
            print(update_task(id_list["id_list"]))

        #Option 3 == delete tasks.
        elif option_user == 3:
            id_list = unique_id()
            print(delete_task(id_list["id_list"]))
        
        
        #Option 4 == status tasks.
        elif option_user == 4:
            id_list = unique_id()
            print(status(id_list["id_list"], option_user))
        
        #Option 5 == delete tasks.
        elif option_user == 5:
            id_list = unique_id()
            print(status(id_list["id_list"], option_user))


        #Option 6 == show all tasks.
        elif option_user == 6:
            id_list = unique_id()
            all_tasks = show_all_tasks()
            pprint.pprint(all_tasks)

        #Option 7 == Show tasks done.
        elif option_user == 7:
            tasks_done = show_tasks_done()
            # print(show_tasks_done())
            pprint.pprint(tasks_done)
        #Option 8 == Show tasks not done.
        elif option_user == 8:
            tasks_not_done = show_tasks_not_done()
            pprint.pprint(tasks_not_done)
        #Option 9 == Show tasks in progress.
        elif option_user == 9:
            tasks_in_progress = show_tasks_in_progress()
            pprint.pprint(tasks_in_progress)

        #Option == 0 Close the script.
        else:
            print("See you next time")
            break

if __name__ == "__main__":
    main()
