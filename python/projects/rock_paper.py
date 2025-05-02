import random 
score_user=0
score_machine=0
print("Welcome to Rock Paper Scissors game")
input("Press Enter to start the game")
print("You will be asked to choose between Rock, Paper and Scissors and quit the game by typing 'q'")
print("Let's start the game")

while True:
    print("rock, paper, scissors?")
    user_input =input("Enter your choice:").lower()

    if user_input == "q":
        print("Thanks for playing!")
        break
    elif user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input, please try again")
        continue
    else:
        machine_input = random.choice(["rock", "paper", "scissors"])
        if user_input == machine_input:
            print("It's a tie!")
        elif (user_input == "rock" and machine_input=="scissors") or (user_input == "paper" and machine_input=="rock") or (user_input == "scissors" and machine_input=="paper"):
            print("You win!")
            score_user += 1
        
        else:
            print("You lose!")
            score_machine += 1

if score_user > score_machine:
    print("You are the winner!")
    print("Your score:" +f"{score_user}"+" Machine score:" +f"{score_machine}")
elif score_user < score_machine:
    print("Machine is the winner!")
    print("Your score:" +"{score_user}"+" Machine score:" +"{score_machine}")
else:
    print("It's a tie!")
    print("Your score:" +"{score_user}"+" Machine score:" +"{score_machine}")