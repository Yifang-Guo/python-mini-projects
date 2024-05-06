import random

exit = False
user_point, computer_point = 0, 0

while exit == False:
    options = ['rock', 'paper', 'scissors']
    user_input = input("please enter rock, paper, scissors or exit \n")
    computer_input = random.choice(options)

    if user_input == 'exit':
        print("game ended.")
        if user_point > computer_point:
            print(f"You win, your points is {user_point}, computer points is {computer_point}")
        elif user_point < computer_point:
            print(f"You lose, your points is {user_point}, computer points is {computer_point}")
        else:
            print(f"It is a tie, you both have {user_point} points")
        exit = True

    if user_input == 'rock':
        print("Your input is rock")
        if computer_input == "rock":
            print("Computer input is rock")
            print("It is a tie")
        elif computer_input == "paper":
            print("Computer input is paper")
            print("Computer wins.")
            computer_point += 1
        elif computer_input == "scissors":
            print("Computer input is scissors")
            print("You win.")
            user_point += 1
    elif user_input == 'paper':
        print("Your input is paper")
        if computer_input == "rock":
            print("Computer input is rock")
            print("You win")
            user_point += 1
        elif computer_input == "paper":
            print("Computer input is paper")
            print("It is a tie.")
        elif computer_input == "scissors":
            print("Computer input is scissors")
            print("Computer wins.")
            computer_point += 1
    elif user_input == 'scissors':
        print("Your input is scissors")
        if computer_input == "rock":
            print("Computer input is rock")
            print("Computer wins")
            computer_point += 1
        elif computer_input == "paper":
            print("Computer input is paper")
            print("You win.")
            user_point += 1
        elif computer_input == "scissors":
            print("Computer input is scissors")
            print("It is a tie.")
    else:
        print("Please enter valid word.")

    
            