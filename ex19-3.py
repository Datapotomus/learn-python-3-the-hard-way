def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def matt_func(pet_name, pet_age):
    print(f"Your pet's name is {str(pet_name)}.")
    print(f"Your pet's age is {pet_age}.")
    print(f"In 2 years {str(pet_name)} will be {pet_age + 2}.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print("Calling matt funct, by just using two parameters.")
matt_func(str("Fin"), 2)

print("Calling pet function now.")
pet_name="Fin"
matt_func(pet_name, 1)

print("#3 providing two variables, then just using them to call.")
pet_name="Layla"
pet_age=12
matt_func(pet_name, pet_age)

#Note!!! I kept getting held up by this, because I kept pushing the string to a string, but the problem was with the pet_age.
#The pet age needed to be an int, because normally the input comes in as a str.
print("#4 Using the user provided input as a call method.")
pet_name_input=input("What's your pets name?")
pet_age_input=int(input("What's your pet's age?"))
matt_func(pet_name_input, pet_age_input)

print("#5 Calling it via just quotes, and a number.")

matt_func("Gizmo", 10)

print("#6 This time making sure to call the function with int as the number.")
matt_func("Finny", int(1))

print("#7 Calling the function, and making sure to define the types for both the arguments.")
matt_func(str('Gizzy'), int(10))

print("#8 Building new variables to combine all the names, and ages of all my pets.")
first_pet="Layla"
second_pet="Gizmo"
thrid_pet="Finny"

first_pet_age=12
second_pet_age=10
third_pet_age=1

pet_name=f"{first_pet} {second_pet}, and {thrid_pet}"
pet_age=int(first_pet_age) + int(second_pet_age) + int(third_pet_age)
print(pet_age)
matt_func(pet_name, pet_age)

print("#9 Doing the same thing, but attempting to put it together in the function call.")
matt_func(str(first_pet + second_pet), int(first_pet_age + second_pet_age))

print("#10 Combining the input variable with the later defined variables.")
matt_func(str(pet_name_input + " " + second_pet), int(pet_age_input + second_pet_age))

