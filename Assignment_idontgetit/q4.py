import random

answer = str(random.randint(1,5))

guess = input("Guess a number between 1 and 5:  ")

#Imported random, so everytime the guess is different
#The I transformed the random number into string to avoid errors
#I decided to put only from 1 to 5, otherwise was too hard to guess
 
if guess == answer:

        print("Lucky!!!")
        print("The number was indeed", answer)

#Show the number, so we can be sure that the answer was correct

elif guess != answer:

        print("Sorry, that’s incorrect.")
        print("The number was", answer)

#Show the number, so we can know what was the number

elif guess:

        print("Something went wrong, please try again.")
