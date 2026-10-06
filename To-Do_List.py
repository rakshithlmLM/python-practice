task = []
print("========== TO-DO LIST ==========")
print("\n1. Add Task\n2. View Task\n3. Delete Task\n4. Exit")


while True:
    try:
        user = int(input("choose: "))
        match(user):
            case 1:
                
                    temp = input("Enter task: ")
                    task.append(temp)
                    print("Task added!")
            case 2:
                if not task:
                    print("No tasks available!")
                else:
                    for number,i in enumerate(task,start=1):
                        print(number,i)
            case 3:
                try:
                    pos = int(input("Enter the number of the task to delete: "))
                    if pos <= 0:
                        print("Enter the Proper Task number!")
                        continue
                    else:
                        del task[pos-1]
                        print("Task Deleted!")
                except IndexError:
                    print("Invaild Task Number!")
            case 4:
                exit(0)
            case _:
                print("Enter the valid choice!!")
    except ValueError:
        print("Enter the valid choice(number)")

        
        