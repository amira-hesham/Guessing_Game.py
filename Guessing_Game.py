# Guessing Game Challenge

#Let's use `while` loops to create a guessing game.

#The Challenge:

#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

#1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"

#2. On all turns, if a guess is 
# * closer to the number than the previous guess return "Closer!"
# * farther from the number than the previous guess, return "Farther!"
#3. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

#Now Lets o fro the Steps!

from random import randint
Actual = randint(1,100) 
Guess= int(input("please enter number from 1 to 100 "))
previous=0
print (Actual)
while 1 :
    if Guess >100 or Guess<1:
        break
    elif abs(Guess-Actual)>abs(previous-Actual):
        print("far guess")
        previous= Guess
        Guess=int(input("please enter number"))
    elif Guess==Actual:
        print(f"{Guess} congratulation")
        break
    else:
        print("close guess")
        previous= Guess
        Guess=int(input("please enter number"))
    
