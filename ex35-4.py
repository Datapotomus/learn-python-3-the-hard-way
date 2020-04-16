from sys import exit

def gold_room():
    print("This room is full of gold how much do you take?")

    choice=input("> ")
    if choice.isdigit():
        how_much=int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much == 0:
        print("You get to go to the super secrect treasure room.")
        secret_room()
    elif how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear in here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice=input("> ")

        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "door" in choice or "through" in choice and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice=input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was Tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice=input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room till you starve.")

def secret_room():
    print("Which treasure would you like?")
    print("The lamp or the jar?")

    choice=input("> ")

    if choice == "lamp":
        print("You get the genie of the lamp! Congradulations!")
        exit(0)
    elif choice == "jar":
        print("You get the genie of the jar! Congradulations!")
        exit(0)
    else:
        dead("You did not choose wisely. The room falls in around you.")



start()