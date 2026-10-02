import random

game_ele = ['rock','paper','scissors']



while True:
    user = input("Choose Rock/Paper/Scissors:").lower()
    computer = random.choice(game_ele)

    print(f"You Chose: {user}")
    print(f"Computer Chose: {computer}")

    if user == computer:
        print("Its a Draw!!")
    elif (
        (user == 'Rock' and computer == 'Scissors') or
        (user == 'Paper' and computer == 'Rock') or
        (user == 'Scissors' and computer == 'Papper')):
            print("You Win!! ")
    else:
        print("Computer Wins!!")

    continue_game = input("Do you want to play another Round? (y/n)").lower()
    if continue_game == 'n':
         print("Thank you dor Playing!!")
         break
    
         

        
