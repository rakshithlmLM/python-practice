import  random
times  = 0
while True:
    choice = input("Do you wnat to roll dice(y/n)").lower()
    if choice == 'y':
        try:
            n = int(input("How many dice Do You want to roll? "))
            if n > 0:
                for i in range(n):
                    roll = random.randint(1,6)
                    print(f"Die ",i+1,":", roll)
                    times += 1
            else:
                print("enyer valid number!!")
        except ValueError:
            print("Enter the number!!")
        
    elif choice == 'n':
        print("Thank you for playing")
        break
    else:
        print("Invaild choice")
print(f"Dice Rolled: {times}")

        




