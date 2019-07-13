fc = input("Input here your favorite color: ").lower()

#giving to the user the possibility to choose the color, we can have more guesses
#we also put everything in lower case, so as long as there is no spelling mistake in the input, the answer from Blue to blue will not change

#if 'b' in favorite_color:

#        if favorite_color == 'blue':
            
# there was a missing = up here, but we won't use it

#               print("Blue is a great color!")

#        elif favorite_color == 'brown':

#               print("Just like the Earth!")

#        else:

#            print("I guess you know more colors than I do.")

#getting rid of the whole part above here, as it's just a duplicate of the code below


if fc == 'blue':

    print("The color of truth.")

elif fc == 'brown':
    
    print("Just like the Earth!")

elif fc == 'red':

    print("Love and passionate!")

elif fc == 'black':

    print("Black is not a color, but darkest shade of grey")

elif fc == 'white':

    print("White is just a grey that is not grey enough...")

elif fc == 'green':

    print("All in one with nature, huh?")

elif fc == 'yellow':

    print("This color represents joy!")

elif fc == 'purple':

    print("A noble color, used to be the most expensive!")

elif fc == 'grey':

    print("Do you even call it color?")

else:

    print("I'm a machine, either you mistyped or who programmed me was too lazy to write down all the colors. ¯\_(ツ)_/¯")

#wrote down in the worst way the different scenarios that the machine can face
