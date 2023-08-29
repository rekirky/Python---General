from requests import Request, Session
import random
guess = 0 
hidden = random.randrange(1, 201)

# add in a counter to see how many tries it takes, increments by one each loop
steps = 0

# Uncomment the next line to display the random number
# print(hidden)  

# while loop. We load in a 0 as the random number won't be it. Then it loops the player entering a number to find the correct one.
while guess != hidden:
    guess = int(input("The random number is between 1 & 200. Please enter your guess: "))
    steps = steps + 1
    if guess == hidden:
        input("Hit! " + str(hidden) + ". You took " + str(steps) + " attempts")
    elif guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")