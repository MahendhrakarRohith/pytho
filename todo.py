# To-Do List Application

# A list to store tasks
todo_list = []

#function for adding task 
def add_task():
    task=input("Enter the task you want to add")
    todo_list.append(task)
    print("your task",task,"added to the list")

#function for removing task
def remove_task():
    task_no=int(input("enter the task number you have to remove : "))
    if 0 < task_no <= len(todo_list):
        remove_task=todo_list.pop(task_no - 1)
        print("your task is removed ")

    else :
        print("invalied task_no")

#function for viewing the task
def view_task():
    if not todo_list:
        print("your list is empty")
    else :
        print("your to do list is :")
        for i,task in enumerate(todo_list):
            print(i,".",task)

#main loop
def main():
    while True:
        print("\n 1.Add task \n 2.Remove task \n 3.View task \n 4.exit")
        choice=int(input("enter your choice : "))

        if choice==1:
            add_task()
        elif choice==2:
            remove_task()
        elif choice==3:
            view_task()
        else:
            print("enter the valied choice")

if __name__=="__main__":
    main()

#end 
