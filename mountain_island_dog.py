#Youth in Action - Python Code

#1. Create a list of cities
cities = ["New York", "Los Angeles", "Chicago", "Philadelphia", "Boston"]

#2. Create a function to display cities
def show_cities(city_list):
        for city in city_list:
            print(city)

#3. Display cities
show_cities(cities)

#4. Create a function to add new cities
def add_city(city_list, new_city):
    if new_city not in city_list: 
        city_list.append(new_city) 

#5. Add a new city
add_city(cities, "San Francisco")

#6. Display updated list
show_cities(cities)

#7. Create a function to remove cities from list
def remove_city(city_list, remove_city):
    if remove_city in city_list:
        city_list.remove(remove_city)

#8. Remove a city
remove_city(cities, "Chicago")

#9. Display updated list
show_cities(cities)

#10. Create a function to sort cities alphabetically
def sort_cities(city_list):
    city_list.sort()

#11. Sort the cities
sort_cities(cities)

#12. Display sorted list
show_cities(cities)

#13. Create a function to calculate the population of each city
def calculate_population(city_list):
    for city in city_list:
        if city == "New York":
            population = 8398748
        elif city == "Los Angeles":
            population = 3990456
        elif city == "Philadelphia":
            population = 1580863
        elif city == "Boston":
            population = 685164
        elif city == "San Francisco":
            population = 884363
        print(city + " has a population of " + str(population) + ".")

#14. Calculate the population of each city
calculate_population(cities)

#15. Create a function to calculate the total population of the cities
def total_population(city_list):
    total = 0
    for city in city_list:
        if city == "New York":
            population = 8398748
        elif city == "Los Angeles":
            population = 3990456
        elif city == "Philadelphia":
            population = 1580863
        elif city == "Boston":
            population = 685164
        elif city == "San Francisco":
            population = 884363
        total += population
    print("The total population of the cities is " + str(total) + ".")

#16. Calculate the total population
total_population(cities)

#17. Create a variable to keep track of the total number of cities
num_cities = len(cities)

#18. Output the number of cities
print("There are " + str(num_cities) + " cities in the list.")

#19. Create a function to count the number of cities with populations over 1 million
def million_population(city_list):
    count = 0
    for city in city_list:
        if city == "New York":
            population = 8398748
        elif city == "Los Angeles":
            population = 3990456
        elif city == "Philadelphia":
            population = 1580863
        elif city == "Boston":
            population = 685164
        elif city == "San Francisco":
            population = 884363
        if population > 1000000:
            count += 1
    print(str(count) + " cities have populations over 1 million.")

#20. Find out how many cities have populations over 1 million
million_population(cities)