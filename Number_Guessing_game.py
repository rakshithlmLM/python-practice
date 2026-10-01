import random

def diff_level():
    print("Choose The Difficulty")
    print("\n1. Easy(1-50)\n2. Normal(1-100)\n3. Hard(1-500)\n4. Exit")
    choice = int(input("Your Choice? \n"))
    match(choice):
        case 1:
            computer = random.randint(1,50)
            mode = "Easy"
        case 2:
            computer = random.randint(1,100)
            mode = "Normal"
        case 3:
            computer = random.randint(1,500)
            mode = "Hard"
        case 4:
            exit(0)
        case _:
            print("Enter a vaild input")
    return mode,computer
def game(computer):
    attempts = 0
    while True:
        try:
            guess = int(input("Guess The Number: "))
            attempts +=1
            if guess == computer:
                print("You win!!")
                break
            elif guess > computer:
                print("Guess Lower!")
            else:
                print("Guess Higher!")
        except ValueError:
            print("Enter Number Only")
    return attempts

mode, computer = diff_level()
attempts = game(computer)

print(f"Difficulty: {mode}")
print(f"You guessed correctly in {attempts} attempts.")
    
