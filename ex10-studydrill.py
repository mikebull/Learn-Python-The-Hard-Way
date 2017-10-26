tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Study Drill 2: Use triple single quptes if you want 
# to add triple double quotes

format_cat = f"""
Much like Backslash Cat, {backslash_cat}
Also, like Fat Cat, {fat_cat}
"""
format_method_cat = "Like \"Persian Cat\", {}".format(persian_cat)

print(format_cat)
print(format_method_cat)