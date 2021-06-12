import random

print("rock...")
print("paper...")
print("scissors...")


player = input("Enter Player's choice: ")

computer = random.randint(1, 3)
if computer == 1:
	computer = "rock"
elif computer == 2:
	computer = "paper"
else:
	computer = "scissors"


print(f"Computer played {computer}...")

if player == "rock" and computer == "paper":
	print("Computer wins!!!")
elif player == "rock" and computer == "scissors":
	print("Player wins!!!")
elif player == "paper" and computer == "rock":
	print("Player wins!!!")
elif player == "paper" and computer == "scissors":
	print("Computer wins!!!")
elif player == "scissors" and computer == "rock":
	print("Computer wins!!!")
elif player == "scissors" and computer == "paper":
	print("Player wins!!!")
elif player == computer:
	print("It's a tie!")
else:
	print("Something went wrong")