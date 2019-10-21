print("Would you like to play a game?")
gameplay=input("> ")

if gameplay == "Y" or gameplay == "y" or gameplay == "Yes" or gameplay == "yes":
    print("OK, lets start.")
    print("Which way do you want to go?")
    print("you see a glowing light up the road, which way do you go?")
    print("1. Towards the light.")
    print("2. Away from the light")
    
    choice=input("> ")

    if choice == "1":
        print("The light is acutally a car that just ran you over.")

    elif choice == "2":
        print("Good choice, you almost got hit by a car.")

    else:
        print("You have to chose one or two.")

elif gameplay == "N" or gameplay == "n" or gameplay == "No" or gameplay == "no":
    print("Maybe we will play next time.")


else:
    print("Why don't you choose another option next time?")
