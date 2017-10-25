# Variable for types of people
types_of_people = 10
# Variable for f-string
x = f"There are {types_of_people} types of people."

# Variable for "binary" string
binary = "binary"
# Variable for "don't" string
do_not = "don't"
# Variable for f-string containing two above string vars
y = f"Those who know {binary} and those who {do_not}."

# Print x f-string
print(x)
# Print y f-string
print(y)

# Print f-string containing f-string in x
print(f"I said: {x}")
# Print f-string containing f-string in y
print(f"I also said: '{y}'")

# Variable for hilarious set to false
hilarious = False
# Variable for joke evaluation containing substitution
joke_evaluation = "Isn't that joke so funny?! {}"

# Print joke evaluation with hilarious placed in substitution by format()
print(joke_evaluation.format(hilarious))

# Set of string variables to concatenate
w = "This is the left side of..."
e = "a string with a right side."

# Print "This is the left side...a string with a right side."
print(w + e)