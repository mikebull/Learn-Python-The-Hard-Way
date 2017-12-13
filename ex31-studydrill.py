print("""You enter a dark room with two doors.
Do you go through door #1, door #2?, or door #3""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Scold the bear for maintaing such an unhealthy diet.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The beat eats your legs off. Good job!")
    elif: bear == "3":
        print("The bear is deeply offended. It's his cheat day.")
        print("He eats you after checking your nutritional info on MyFitnessPal. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You see a table. On the table is a sandwich.")
    print("1. Eat the sandwich.")
    print("2. Eat the table.")

    food = input("> ")

    if food == "1":
        print("Your teeth shatter. That was no sandwich! It was a brick.")
    if food == "2":
        print("Well done! The table was actually a large table-shaped cake. Yum!")
    else:
        print("The uncertainty overwhelms you, and you are carted off to an asylum.")

else:
    print("You stumble around and fall on a knife and die. Good job!")