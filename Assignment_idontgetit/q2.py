def power_up(x, power = 2):

        val = x ** power

        return val

 

print(power_up(3, power = 3))

#in this way, the solution will be 27, ergo, 3**3
#the mistake was the misplacement of the two values
#I could have used also just power_up(3, 3) in the print line, that would've worked too

