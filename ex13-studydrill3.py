from sys import argv

script, firstname, lastname = argv
nickname = input("What is your nickname? ")

print("Your name is {} \"{}\" {}!".format(firstname, nickname, lastname))