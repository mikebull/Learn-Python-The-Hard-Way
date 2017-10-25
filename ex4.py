# Set cars variable
cars = 100
# Set space in a car variable
space_in_a_car = 4.0
# Set drivers variable
drivers = 30
# Set passengers variable
passengers = 90
# Set cars not driven variable
cars_not_driven = cars - drivers
# Set cars driven variable
cars_driven = drivers
# Set carpool capacity variable
carpool_capacity = cars_driven * space_in_a_car
# Set average passengers per car variable
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")