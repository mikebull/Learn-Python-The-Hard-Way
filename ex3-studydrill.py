# Print "I will not count my chickens:"
print("I will now count my chickens:")

# Print the number of Hens
print("Hens", 25 + 30 / 6)
# Print the number of Roosters
print("Roosters", 100 - 25 * 3 % 4)

# Print "Now I will count the eggs:"
print("Now I will count the eggs:")

# Print calculation of the number of eggs
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Print "Is it true that 3 + 2 < 5 - 7?"
print("Is it true that 3 + 2 < 5 - 7?")

# Print calculation
print(3 + 2 < 5 - 7)

# Print "What is 3 + 2?", followed by the calculation
print("What is 3 + 2?", 3 + 2)
# Print "What is 5 - 7?", followed by the calculation
print("What is 5 - 7?", 5 - 7)

# Print "Oh, that's why it's False."
print("Oh, that's why it's False.")

# Print "How about some more."
print("How about some more.")

# Print "Is it greater?", followed by the calculation
print("Is it greater?", 5 > -2)
# Print "Is it gresater or equal?", followed by the calculation
print("Is it greater or equal?", 5 >= -2)
# Print "Is it less or equal?", followed by the calculation
print("Is it less or equal?", 5 <= -2)

# Study Drill 3: Find something you need to calculate and
# write a new .py file that does it.

print(100 + 0 + 250)
print(25 - 50)
print(100 / 5)
print(100 * 5)
print(100 % 5)
print(50 < 25)
print(25 > 50 - 25)
print(50 <= 25 + 25)
print(25 >= 50)

# Study Drill 4: Rewrite ex3.py to use floating point numbers
# so it's more accurate. 20.0 is floating point. 

from decimal import Decimal

print(16/7)
print(Decimal(16/7))