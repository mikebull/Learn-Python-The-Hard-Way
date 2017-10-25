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

# Study Drill 0: Error message states that car_pool_capacity 
# is not defined because the variable name is carpool_capacity. 
# When the code looked for the variable definition it was unable 
# to find the correct one, and it threw a NameError.

# Study Drill 1 & 2: The resulting value will be a floating point 
# number. As we are doing multiplication in Python 3 there will 
# be no change to the number it represents.