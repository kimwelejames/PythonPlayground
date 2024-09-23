from countryinfo import CountryInfo

country_name = input("Enter country Name: ")
country = CountryInfo(country_name)

print("Country Name:", country.name())
print("Capital:", country.capital())
print("Population:", country.population())
print("Currencies:", country.currencies())
print("Area:", country.area())
population = country.population()
area = country.area()
if population and area:
    density = population / area
    print("Density:", density)
else:
    print("Density: Data not available")
print("Languages:", country.languages())
print("Region:", country.region())
print("Borders:", country.borders())
print("Demonym:", country.demonym())
