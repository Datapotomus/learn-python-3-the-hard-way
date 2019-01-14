# Defining format variable with {} to put a value in.
formatter = "{} {} {} {}"

#printing 1 2 3 4 by inserting those text values into value slots.
print(formatter.format(1, 2, 3, 4))
#printing the words instead of the numbers the same way.
print(formatter.format("one", "two", "three", "four"))
#printing boolean values for each of the four slots.
print(formatter.format(True, False, False, True))
#printing out the variable four times. Since the variable is {} {} {} {}, it will duplicate it 4 times.
print(formatter.format(formatter, formatter, formatter, formatter))
#printing each of the values, since the variable is on one line it will combine them back together even though they are on seperate lines.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# Adding more comments.
'''
Adding a block comment
'''

print(formatter.format("This", "works", "by", "variables."))