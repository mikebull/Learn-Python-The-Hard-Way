# Define function to print how many cheese and 
# crackers are available for a party
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Define function to output a list of 
# cheeses to the terminal
def output_all_cheeses(*args):
    if len(args) > 0:
        print(f"You have brought {len(args)} cheeses with you:")
        for arg in args:
            print("* {}".format(arg))
        print("Thank you!\n")
    else:
        print("You have brought no cheese with you. Boo!")

# Call function with numbers provided directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Assign int values to variables and pass to function.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call function with calculations passed
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Call function with calculations based on variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

babybell = "Babybell"
brie = "Brie"
cheddar = "Cheddar"
camembert = "Camembert"

output_all_cheeses("Brie", "Cheddar")
output_all_cheeses()
output_all_cheeses(cheddar, babybell)
output_all_cheeses("Brie", cheddar)