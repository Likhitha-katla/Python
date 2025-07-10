todo_list = [] 

def add_task():
    new_task = input("enter the task")
    todo_list.append({ "task":new_task , "status":"pending" })
    print("New task added succesfully")

def view_tasks():
    if len(todo_list) == 0:
        print("No tasks to do")
    else:
        # for i in todo_list:
        #     print(i["task"])
        for index , task in enumerate(todo_list):
            print(f" { index + 1 } : { task['task'] } - { task['status']} ")

def mark_complete():
    if( len(todo_list) == 0 ):
        print(" All tasks are completed ")
    else:
        view_tasks()
        try:
            mark_task_no = int(input("enter the task to mark complete")) - 1
            if 0 <= mark_task_no < len(todo_list):
                if todo_list[mark_task_no]["status"] == "completed":
                    print("Already Status is completed")
                else:
                    todo_list[mark_task_no]["status"] = "completed"
                    print(f"Task marked as completed: {todo_list[mark_task_no]['task']}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Invalid task number")


def delete_task():
    if len(todo_list) == 0:
        print("No tasks")
    else:
        view_tasks()
        try:
            remove_task_no = int(input("enter the task to delete")) - 1
            if 0 <= remove_task_no < len(todo_list):
                remove_task = todo_list.pop(remove_task_no)
                print(f"Task removed : {remove_task['task']}")
                # print(len(todo_list))
            else:
                print("Invalid task number")
        except Exception as e:
            print(e)



def Main():
    while(True):
        print()
        print("1.Add task") 
        print("2.View existing tasks")
        print("3.Mark tasks as complete")
        print("4.Delete tasks")
        print("5.Exit")
        try:
            val = int(input("enter your choice"))
            if val == 1:
                add_task()
            elif val == 2:
                view_tasks()
            elif val == 3:
                mark_complete()
            elif val == 4:
                delete_task()
            elif val == 5:
                print("exit of application")
                break
            else:
                print("please choose from above options only")
        except Exception as e:
            print(f"please choose from above options only {e}")
Main()