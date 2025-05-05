import random  

print("Welcome to Pig game")
player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")
print("roll the dice or hold type 'r' or 'h'")
print("let's start the game")

while True:
    player1_score=0
    player2_score=0
    play_turn = player1
    while True:
        choice =input(f"{play_turn}, press 'r' to roll the dice or 'h' to hold:").lower()
        if choice == "r":
            roll = random.randint(1, 6)
            print(f"{play_turn} rolled a {roll}")
            if roll == 1:
                player1_score = 0
                if play_turn == player1:
                    play_turn = player2
                    print(f"{player1} score is {player1_score}")
                else:
                    play_turn =  player1
                    print(f"{player2} score is {player2_score}")
            else:
                if play_turn == player1:
                    player1_score += roll
                    print(f"{player1} score is {player1_score}")
                else:
                    player2_score += roll
                    print(f"{player2} score is {player2_score}")
        elif choice == "h":
            if play_turn == player1:
                play_turn = player2
                print(f"{player1} score is {player1_score}")
            else:
                play_turn = player1
                print(f"{player2} score is {player2_score}")
        else:
            print("Invalid input, please try again")
            continue
        if player1_score >= 50:
            print(f"{player1} wins!")
            break
        elif player2_score >= 50:
            print(f"{player2} wins!") 
            break
        else:
            continue
    
    break
print("Thanks for playing!")
                