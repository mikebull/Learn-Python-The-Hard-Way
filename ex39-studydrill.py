# create a mapping of country to abbreviation
uk_countries = {
    "England": "ENG",
    "Northern Ireland": "NIR",
    "Scotland": "SCO",
    "Wales": "WAL"
}

# create a basic set of countries and some cities in them
uk_cities = {
    "ENG": "Bristol",
    "SCO": "Glasgow",
}

# add some more cities
uk_cities['WAL'] = 'Swansea'
uk_cities['NIR'] = "Londonderry"

# print out some cities
print('-' * 10)
print("England has: ", uk_cities['ENG'])
print("Wales has: ", uk_cities['WAL'])

# print some countries
print('-' * 10)
print("Scotland's abbreviation is: ", uk_countries['Scotland'])
print("Northern Ireland's abbreviation is: ", uk_countries['Northern Ireland'])

# do it by using the country then cities dict
print('-' * 10)
print("Scotland has: ", uk_cities[uk_countries['Scotland']])
print("Northern Ireland has: ", uk_cities[uk_countries['Northern Ireland']])

# print every country abbreviation
print('-' * 10)
for country, abbrev in list(uk_countries.items()):
    print(f"{country} is abbreviated {abbrev}")

# print every city in country
print('-' * 10)
for abbrev, city in list(uk_cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for country, abbrev in list(uk_countries.items()):
    print(f"The country {country} is abbreviated {abbrev}")
    print(f"and has city {uk_cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by country that might not be there
country = uk_countries.get('Sealand')

if not country:
    print("Sorry, no Sealand.")

# get a city with a default value
city = uk_cities.get('SEL', 'Does not Exist')
print(f"The city for the country 'SEL' is {city}")