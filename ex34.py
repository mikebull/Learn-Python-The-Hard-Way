animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

def choose_animal(choice):
    """Selects an animal from the list."""
    choice = int(choice)

    if choice == 1:
        postfix = "st"
    elif choice == 2:
        postfix = "nd"
    elif choice == 3:
        postfix = "rd"
    else:
        postfix = "th"

    animal = animals[choice-1]

    print(f"The {choice}{postfix} animal is at {choice-1} and is a {animal}.")
    print(f"The animal at {choice-1} is the {choice}{postfix} animal and is a {animal}")

print("Pick your animal:")

number = input("> ")

choose_animal(number)