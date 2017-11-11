# Import argv from the sys module
from sys import argv

# Assign the terminal arguments to the 
# script and input_file variables
script, input_file = argv

# Function to print the contens of f
def print_all(f):
    print(f.read())

# Function to move file reader to the
# first byte of the file.
def rewind(f):
    f.seek(0)

# Function to print a line of the 
# provided file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open file and assign to current_file variable
current_file = open(input_file)

# Print "First let's print the whole file\n"
print("First let's print the whole file:\n")

# Print contens of file using print_all() function
print_all(current_file)

# Print "Now let's rewind, kind of like a tape."
print("Now let's rewind, kind of like a tape.")

# Return file to start using rewind() function
rewind(current_file)

# Print "Let's print three lines!"
print("Let's print three lines!")

# Assign 1 to current_line variable
current_line = 1
# Print current line using print_a_line() function
print_a_line(current_line, current_file)

# Add 1 to current_line value
current_line = current_line + 1
# Print current line using print_a_line() function again
print_a_line(current_line, current_file)

# Add 1 to current_line value
current_line = current_line + 1
# Print current line using print_a_line() 
# function a third time
print_a_line(current_line, current_file)