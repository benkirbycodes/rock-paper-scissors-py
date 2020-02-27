# Rock Paper Scissors Console Game

# Setup
import random
randomInt = random.randint(1, 3)

choices = {"rock": 1, "paper": 2, "scissors": 3}

# User Messages & Input

print("ROCK PAPER SCISSORS")
print("---------------------""\n")
name = input("What is your name?  \n")
print("Nice to meet you " + name + "\n")
choice = input("Rock, Paper or Scissors?")

choices[choice.lower()]
