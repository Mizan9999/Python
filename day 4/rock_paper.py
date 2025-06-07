import random
game = ["rock", "paper", "scissors"]
pc_select = game[random.randint(0,2)]
my_select = input("Whats you select? rock, paper, scissors\n")

if my_select == "rock" and pc_select == "scissors":
    print("You Won the game!")
elif my_select == "paper" and pc_select == "rock":
    print("You Won the game!")
elif my_select == "scissors" and pc_select == "paper":
    print("You Won the game!")
elif my_select == "rock" and pc_select == "rock":
    print("Draw!")
elif my_select == "paper" and pc_select == "paper":
    print("Draw")
elif my_select == "scissors" and pc_select == "scissors":
    print("draw")
else:
    print("you lose the game!")

print(f"\n \n{pc_select}")