def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# My Own function
def mattfunc(a, b):
    print(f"Doing some Matt stuff with {a} and {b}")
    return (a + b) * a

def mattfunc2(firstarg, secarg):
    print(f"mattfunc2 now has values for firstarg={firstarg} and secarg={secarg}",
    "We are going to do some maths on them.")
    return iq - firstarg - secarg

print("Let's do sowme math with just functions!")

age=add(30, 5)
height=subtract(78, 4)
weight=multiply(90, 2)
iq=divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what=add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes", what, "Can you do it by hand?")

# Interesting thing to note is that even if you just define a variable that isn't currently being used it will still invoke the function.
print("This is before the var.")
matt=mattfunc(2, 4)
print("This is after the var.")

print("This is calling the var again.")
matt2=mattfunc(2, 2)
print("This is ending the call again.")

print(f"Matt's function is equals: {matt}")
print(f"Matt2 function equals: {matt2}")

matt2=mattfunc2(2, 2)
print("I am reassigning matt2 to the second matt function now")
print(f"matt2 now equals {matt2} even though it was used in the variable above.")

print("Testing mattfunc2 with new arg values.")
matt2=mattfunc2(4, 4)
