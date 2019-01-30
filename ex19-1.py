#inital definition of the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
#invoking the function, and giving it two inputs that it will essentially make variables.
cheese_and_crackers(20, 30)


#providing the two variables, and then just feeding them to the function.
print("OR, we can use variables from our script:")
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Doing math first, then sending the result of that math as a variable to the function.
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#taking the variables above on line 16 and 17, then doing math on them. Then sending those values to the functions.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)