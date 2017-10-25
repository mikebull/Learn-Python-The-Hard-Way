# Assign string with substitution braces to formatter variable
formatter = "{} {} {} {}"

# Print "1 2 3 4"
print(formatter.format(1, 2, 3, 4))
# Print "one two three four"
print(formatter.format("one", "two", "three", "four"))
# Print "True False False True"
print(formatter.format(True, False, False, True))
# Print "{} {] {] {] {} {] {] {] {} {] {] {] {} {] {] {]"
print(formatter.format(formatter, formatter, formatter, formatter))
# Print "Try your Own text here Maybe a poem Or a song about fear"
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))