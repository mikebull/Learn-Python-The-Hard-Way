from sys import argv

# Testing logical operators first
print("Logical Operators:\n")

if True and False:
    print("True and False should never print")

if True or False:
    print("True or False should print")

if False and False:
    print("False and False should  never print")

if False or False:
    print("False or False should never print")

if True or True:
    print("True or True should print")

if True and True:
    print("True and True should print")

if not(True and True):
    print("Not True and Not True should never print")

# Testing "is"
print("\nThe \"is\" keyword:\n")

if True is True:
    print("True is True equals True")

if False is False:
    print("False is False equals True")

empty_list_1 = []
empty_list_2 = []



# Looping
print("\nFor and While loops\n")
numbers = [0, 1, 2, 3]

for number in numbers:
    print(f"Number: {number}")

count = 0

while count < len(numbers):
    print(f"Number: {count}")
    count += 1

# Try/Except/Finally
print("\nTry/Except/Finally\n")
num_value = "5"
char_value = "test"

try:
    num_value = int(num_value)
except:
    print("This should be fine, as num_value is a valid integer.")

try:
    num_value = int(char_value)
except:
    print(f"The value \"{char_value}\" is not a valid integer.")
finally:
    print("That's all, folks!")

# With/As
print("\nWith/As:\n")
with open("test.txt") as f:
    print(f.read())

# Class/Elif/Pass
class Pizza:
    """Class describing a Pizza."""

    def __init__(self):
        """Constructor."""
        self.toppings = []
    
    def add_topping(self, topping):
        """Adds a topping to the pizza."""
        self.toppings.append(topping)
        print(f"Added {topping} to pizza.")

    def check_topping(self, topping):
        if topping in self.toppings:
            print(f"There is {topping} on this pizza.")
        else:
            print(f"There is no {topping} on this pizza.")

    def number_of_toppings(self):
        """Output number of toppings on pizza."""
        return len(self.toppings)
    
    def list_toppings(self):
        """Prints a list of all the toppings on the pizza."""
        if len(self.toppings) == 1:
            print(f"This pizza only has {self.toppings[0]}. That's a bit bland!")
        elif len(self.toppings) > 1:
            topping_str = ", ".join(self.toppings)
            print(f"This pizza is topped with {topping_str}. Delicious!")
        else:
            print("This pizza has no toppings yet.")

    def not_impl_method():
        """Example of not implemented method using pass keyword."""
        pass

print("\nClass/Elif/Pass:\n")

cheese_pizza = Pizza()
cheese_pizza.add_topping("Cheese")
cheese_pizza.check_topping("Chicken")
cheese_pizza.list_toppings()

print(f"The cheese pizza has {cheese_pizza.number_of_toppings()} toppings")

pizza = Pizza()
pizza.add_topping("Cheese")
pizza.add_topping("BBQ Sauce")
pizza.add_topping("Chicken")
pizza.add_topping("Peppers")
pizza.add_topping("Onions")
pizza.check_topping("Chicken")
pizza.list_toppings()

print(f"The BBQ Chicken pizza has {pizza.number_of_toppings()} toppings.")

# Assert/Raise
print("\nAssert/Raise:\n")

i = 5
higher = 6

try:
    assert i > higher
except AssertionError:
    print(f"Incorrect assertion. {i} is not higher than {higher}.")

try:
    print("Now, let's divide. Give me a number to divide by:")
    i = int(input("> "))
    if i == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    else:
        print("Well done! You picked a number we can divide by!")
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print(f"Invalid number: {i} is not a number!")

# Del
print("\nDel:\n")

a = [1, 2, 3, 4, 5]

print("Iniital List:", ", ".join(str(x) for x in a))

del a[0]

print("New List:", ", ".join(str(x) for x in a))

# Is
print("\nIs:\n")

test_text_1 = "Test"
test_text_2 = "Test"

if test_text_1 == test_text_2:
    print("This should print.")

if test_text_1 is test_text_2:
    print("This also should.")

test_list_1 = [1, 2, 3]
test_list_2 = [1, 2, 3]

if test_list_1 == test_list_2:
    print("This should print.")

if test_list_1 is test_list_2:
    print("This shouldn't.")

# Break/Continue/Lambda
print("\nBreak/Continue/Lambda:\n")

print("This will print 1..10, but will stop at 5")
j = lambda k: print(k)

for i in range(1, 11):
    if i == 6:
        break
    j(i)

print("This will print 1..10, but will skip 5")
for i in range(1, 11):
    if i == 5:
        continue
    j(i)

# Exec
print("\nExec:\n")

print("Let's execute a sum:")
exec("print('5 + 5 =', 5 + 5)")

# Global
print("\nGlobal:\n")

i = 5

def add_five():
    global i
    i += 5

print(f"i is {i}")

add_five()

print(f"Now i is {i}")

# Yield
print("\nYield:\n")

print("Let's generate some sequences:")

def quadratic_sequence():
    for i in range(10):
        yield i * i

for i in quadratic_sequence():
    print(i)