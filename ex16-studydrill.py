# Import argv from sys module
from sys import argv

# Take two arguments from terminal: one being the 
# script, and the other being the name of 
# the txt file to pass in.
script, filename = argv

# Open file with read permissions
target = open(filename, "r")

# Read existing contents of file
content = target.read()

# Print explanation, and contents of txt file
print(f"The file currently {filename} contains the following:")
print(content)

# Print prompts
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Use input to await instruction
input("?")

# Print "Opening the file..."
print("Opening the file...")
# Open file with write permissions and 
# assign to target variable.
target = open(filename, 'w')

# Print "Truncating the file. Goodbye!"
print("Truncating the file. Goodbye!")
# Empties file
target.truncate()

# Print "Now I'm going to ask you for three lines."
print("Now I'm going to ask you for three lines.")

# Ask for several lines input, and 
# assign to separate variables.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Print "I'm going to write these to the file."
print("I'm going to write these to the file.")

# Write contents of line variables to file.
target.write("{}\n{}\n{}\n".format(line1, line2, line3))

# Print "And finally, we close it."
print("And finally, we close it.")
# Close the file.
target.close()