travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new_dict = {}
    new_dict["country"] = country
    new_dict["visits"] = visits
    new_dict["cities"] = cities
    travel_log.append(new_dict)

# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
