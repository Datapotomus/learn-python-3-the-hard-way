people=10
cars=40
trucks=15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
 
if cars > people and trucks > cars:
    print("We have more cars, and more trucks.")
elif cars > people and trucks < cars:
    print("We have more cars and less trucks than cars.")
elif cars < people or trucks > people:
    print("We have less cars than people, but more trucks than people.")
else:
    print("Just make a decision!")