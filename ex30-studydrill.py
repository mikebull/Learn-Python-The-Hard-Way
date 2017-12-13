people = 30
cars = 40
trucks = 15


if cars > people:
    # If there are more cars than people
    print("We should take the cars.")
elif cars < people:
    # Otherwise, if there are more people than cars
    print("We should not take the cars.")
else:
    # If neither of the above are true, do this.
    print("We can't decide.")

if trucks > cars:
    # If there are more trucks than cars
    print("That's too many trucks.")
elif trucks < cars:
    # Otherwise, if there are more cars than trucks
    print("Maybe we could take the trucks.")
else:
    # If neither of the above are true, do this.
    print("We still can't decide.")

if (cars > people) and (trucks < cars):
    # If there are more cars than people, and more cars than trucks
    print("We should definitely take the cars.")
elif (cars > people) or (trucks < cars):
    # If there are more cars than people, or more cars than trucks
    print("It's between cars and trucks.")
else:
    print("Oh, I'm not sure.")


if people > trucks:
    # If there are more people than trucks
    print("Alright, let's just take the trucks.")
else:
    # Otherwise, do this.
    print("Fine, let's stay home then.")