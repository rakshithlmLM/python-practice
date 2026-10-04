import random

game_ele = ['rock','paper','scissors']

user_win = 0
draw = 0
computer_win = 0


while True:
    user = input("Choose Rock/Paper/Scissors:").lower()
    
    if user not in game_ele:
         print("Enter the Valid Option(rock/paper/scissors)")
    else:
        computer = random.choice(game_ele)
        print(f"You Chose: {user}")
        print(f"Computer Chose: {computer}")

        if user == computer:
            print("Its a Draw!!")
            draw +=1
        elif (
            (user == 'rock' and computer == 'scissors') or
            (user == 'paper' and computer == 'rock') or
            (user == 'scissors' and computer == 'paper')):
                print("You Win!! ")
                user_win +=1
        else:
            print("Computer Wins!!")
            computer_win +=1

        continue_game = input("Do you want to play another Round? (y/n)").lower()
        if continue_game == 'n':
            print("Thank you dor Playing!!")
            break
        elif continue_game == 'y':
            continue
        else:
            print("Enter Vaild input next time!! ")
            break 
print("===========Score===============") 
print(f"You won {user_win} times")
print(f"computer won {computer_win} times")
print(f"draw {draw} times")
print("===========Final Results=========")
if user_win > computer_win:
     print("You have won the game!")
elif computer_win > user_win:
     print("Computer has won the game!\nBetter Luck Next Time!")
else:
     print("Overall game was a draw!!")

         

        
