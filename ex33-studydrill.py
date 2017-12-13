def loop_numbers(limit, increment):
    """Loop through numbers 0-limit in specified increments."""
    i = 0
    numbers = []

    for i in range(0, limit, increment):
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    return numbers

limit = 6
increment = 2

numbers = loop_numbers(limit, increment)

print("The numbers: ")

for num in numbers:
    print(num)