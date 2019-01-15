name=input("Please enter your name: ")
print("Hello, ", name)

o=input(f"{name}, Please provide me with an object: ")
print(name, ", the object you entered is a ", o)

x=input(f"Now {name}, can you provide me with another object: ")
print("The second object you provided is a(n) " + x)

print(name, f""", you have provided me the following information:
\tYour first object is a {o}
\tYour second object is a {x}
""")