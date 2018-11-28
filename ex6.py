#SnS = String in a string.
# A variable declaring the number 10 as it's value.
types_of_people = 10
#Another variable with a string, and a variable inside the string with the "f" signaled.
x = f"There are {types_of_people} types of people." #SnS

# A variable named binary , that has a string "binary as it's value."
binary = "binary"
# A variable name do_not, with a string that is "don't" as it's value.
do_not = "don't"
# A variable "y", that has a string with two inserted variables.
y = f"Those who know {binary} and who {do_not}." #SnS

# Both statements are printing out each of the variable so they show up on screen.
print(x)
print(y)

# printing a string with x variable inserted, which also chains together the "types_of_people" variable.
print(f"I said: {x}") #SnS + SnS(x)
#printing a string with y variable that also pulls in the binary and do_not variable as well.
print(f"I aslo said: '{y}'") #SnS + SnS(y)

#Setting a boolean value for hilarious.
hilarious = False
#This variable is a string, and also allows another variable to be called inside of it.
joke_evaluation = "Isn't that joke so funny?! {}" #S into a variable (might not be a string)

#printing the joke_evaluation variable, then applying a format, then inserting the "hilarious" variable into the end of the print string. Doc says that it is part of the already created string, which is joke_evaluation.
print(joke_evaluation.format(hilarious)) #This causes it to be a string in a string, due to format.

# w variable that has the string text as the thing its assigned.
w = "This is the left side of..."
# e variable with more string text that it is assigned.
e = "a string with a right side."

# A print statment that combines the w variable with the e variable.
print(w + e)