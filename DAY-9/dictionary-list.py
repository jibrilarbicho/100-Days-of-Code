travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def add_newCountry(country_visited, times_visited, cities_visited):
    newCountry = {}
    newCountry["country"] = country_visited
    newCountry["visits"] = times_visited
    newCountry["cities"] = cities_visited
    travel_log.append(newCountry)


add_newCountry("Russia", 2, ["Moscow", "Saint Petersburg"])


print(travel_log)
