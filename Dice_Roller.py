import  random
while True:
    choice = input("Do you wnat to roll dice(y/n)").lower()
    if choice == 'y':
        n = int(input("How many dice Do You want to roll? "))
        for i in range(n):
            roll = random.randint(1,6)
            print(f"Die :",i+1, roll)
    elif choice == 'n':
        print("Thank you for playing")
        break
    else:
        print("Invaild choice")

        




