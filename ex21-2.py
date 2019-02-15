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


print("Let's do sowme math with just functions!")

age=add(30, 5)
height=subtract(78, 4)
weight=multiply(90, 2)
iq=divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what=add(age, subtract(height, multiply(weight, divide(iq, 2))))
#To break this apart, you start with the smallest paren, and work your way backward.
# iq=divide(100, 2)
# iq=50
# divide(50, 2)
# divide= 25
# weight=90*2
# weight=180
# Multiply=180, 25
# multiply=4500
#height=78-4
#height=74
#subtract=74-4500
#subtract=-4426
#age=30+5
#age=35
#add=35+-4426
#add=-4391

print("That becomes", what, "Can you do it by hand?")