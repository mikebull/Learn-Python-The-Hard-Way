people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats. The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

cats += 10

if (dogs < cats) and (cats >= people):
    print("People are doomed! The cats are taking over the world!")

if (dogs > cats) and (people <= cats):
    print("The world is safe. The dogs will protect us.")

dogs += 10

if dogs == cats:
    print("The great Dogs vs Cats war has begun!")

people -= 20

if people != 0:
    print("The human race is safe.")
else:
    print("The humans are dead. Long live the cats!")