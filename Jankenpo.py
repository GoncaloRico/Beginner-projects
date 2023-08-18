import random
#r>s s>p p>r

def play():
    stop = False
    play_again = "y"
    score_user = 0
    score_computer = 0
    user = ""
    while stop == False:
        user = input("Select Rock (R), Paper (P) or Scissors (S): ").lower()
        computer = random.choice(["r", "p", "s"])
        if user == computer:
            print("It's a tie!")
            play_again = input(f"Current score is: You {score_user} - {score_computer} Computer. Do you want to play again? Pick Yes (Y) or No (N): ").lower()

        if user != "r" and user != "p" and user != "s":
            print("Invalid choice! Please type 'R', 'P' or 'S'!")

        if (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
            print(f"Congratulations, you win! Computer picked scissors.")
            score_user = score_user + 1
            play_again = input(f"Current score is: You {score_user} - {score_computer} Computer. Do you want to play again? Pick Yes (Y) or No (N): ").lower()

        if (user == "r" and computer == "p") or (user == "p" and computer == "s") or (user == "s" and computer == "r"):
            print(f"Aw shucks, you lose! Computer picked paper.")
            score_computer = score_computer + 1
            play_again = input(f"Current score is: You {score_user} - {score_computer} Computer. Do you want to play again? Pick Yes (Y) or No (N): ").lower()

        if play_again != "n" and play_again != "y":
            print("Invalid choice! Please type 'Y' or 'N'!")

        if play_again == "n":
            print(f"Thank you for playing! The final score is: You {score_user} - {score_computer} Computer! Come back for a rematch!")
            stop = True

play() 

        

