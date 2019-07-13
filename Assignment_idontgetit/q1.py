answer = str(5)

#By transforming the integer in string, we avoid collisions between int() and str()

guess = input("Guess a number between 1 and 10:  ")



if guess == answer:

        print("Great job!")

elif guess != answer:

        print("Sorry, that’s incorrect.")

else:

        print("Something went wrong, please try again.")
