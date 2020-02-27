# Rock Paper Scissors Console Game

# Setup
import random
randomInt = random.randint(1, 3)

choices = {"rock": 1, "paper": 2, "scissors": 3}
computerChoices = {1: "Rock", 2: "Paper", 3: "Scissors"}

# User Messages & Input

print("ROCK PAPER SCISSORS")
print("---------------------""\n")

name = input("What is your name?  \n")

print("Nice to meet you " + name + "\n")

choice = input("Rock, Paper or Scissors?\n")
choiceInt = choices[choice.lower()]
computerChoiceText = computerChoices[randomInt]

if choices.get(choice.lower()) == None:
    print("That's not an option")
elif (choiceInt + 1) % 3 == randomInt:
    print("Computer's Choice: " + computerChoiceText + "\n")
    print("Computer Wins!\n")
elif choiceInt == randomInt:
    print("Computer's Choice: " + computerChoiceText + "\n")
    print("It's A Draw!\n")
else:
    print("Computer's Choice: " + computerChoiceText + "\n")
    print("You win!\n")
