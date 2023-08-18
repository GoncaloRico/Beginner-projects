import random
outcome = {"r":"Scissors", "p":"Rock", "s":"Paper"} #This dictionary contains all the pairs of win conditions
play_again = "y"
score_user = 0
score_computer = 0
user = ""

def play():
    play_again = "y"
    score_user = 0
    score_computer = 0
    user = ""
    while play_again == "y":
        user = input("Select Rock (R), Paper (P) or Scissors (S): ").lower()
        computer = random.choice(["Rock", "Paper", "Scissors"])

        if user not in {"r", "p", "s"}:
            print("Invalid choice! Please type 'R', 'P' or 'S'!")
            continue

        elif user == computer:
            print("It's a tie!")

        elif outcome[user] == computer: #This will match up the user's input with it's correspondence in our "outcome dictionary". 
                                        #For example, if the user picks Rock (r), it's corresponding element in "outcome" would be "Scissors". If that's what the computer picked, it's a win for the user!
            print(f"Congratulations, you win! Computer picked {computer}.")
            score_user += 1

        else:
            print(f"Aw shucks, you lose! Computer picked {computer}.")
            score_computer += 1

        while True:
            play_again = input(f"Current score is: You {score_user} - {score_computer} Computer. Do you want to play again? Pick Yes (Y) or No (N): ").lower()

            if play_again == "n":
                print(f"Thank you for playing! The final score is: You {score_user} - {score_computer} Computer! Come back for a rematch!")
                break
            
            elif play_again == "y":
                break
            
            print("Invalid choice! Please type 'Y' or 'N'!")

play() 

        

