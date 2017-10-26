print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("\nWhat day of the month were you born in?")
day = input("-> ")
print("What month were you born in?")
month = input("--> ")
print("Finally, what year were you born in?")
year = input("---> 19")

print("So, your birthday is {} {} 19{}.".format(day, month, year))