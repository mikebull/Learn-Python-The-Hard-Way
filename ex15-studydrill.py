# Import argv from the sys module
from sys import argv

# Get the script name and the file name 
# from the terminal arguments
script, filename = argv

# Open the file and assign to txt variable
txt = open(filename)

# Print "Here's your file ex15_sample.txt"
print(f"Here's your file {filename}:")
# Print the contents of the provided file
print(txt.read())

# Close the file
txt.close()

# Print "Type the filename again:"
print("Type the filename again:")
# Prompt for user input and assign to variable
file_again = input("> ")

# Open the file and assign to txt_again variable
txt_again = open(file_again)
# Print the contents of the provided file
print(txt_again.read())

# Close the file
txt_again.close()