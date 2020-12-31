print("----welcome to rock paper scissors game----")
import random
randomNumber = random.randint(0, 2)
if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissors"
personW = 0
computerW = 0
finalScore = 5
while personW < finalScore and computerW < finalScore:
    print(f"person wins is : {personW} & computerW is : {computerW} ")
    player_1 = input("Enter your move => ")
    player_2 = print(f"Computer enter your move => {computerMove} ")
    player_2 = computerMove
    if player_1 == player_2:
        print("That is tie")
    elif player_1 == "q" or player_1 == "quit":
        break
    elif player_1 == "rock":
        if player_2 == "paper":
            print("player_2 wins")
            computerW += 1
        elif player_2 == "scissors":
            print("player_1 wins")
            personW += 1
    elif player_1 == "paper":
        if player_2 == "rock":
            print("player_1 wins ")
            personW += 1
        elif player_2 == "scissors":
            print("player_2 wins ")
            player_2 += 1
    elif player_1 == "scissors":
        if player_2 == "rock":
            print("player_2 wins ")
            computerW += 1
        elif player_2 == "paper":
            print("player_1 wins ")
            personW += 1
    else:
        print("something went wrong\n Try again")

print(f"finalScores=> person wins : {personW} & computer wins : {computerW}")

