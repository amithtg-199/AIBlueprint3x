travel_log = {
    "France": ["paris","lille", "Dijon"],
    "Germany": ["Berlin","Munich"]
}

print(travel_log["France"][1])

nested_list = ["a", "b", ["c","d"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_time_visited": 8,
        "cities_vistied": ["paris","lille", "Dijon"]
    },
    "Germany": ["Berlin","Munich"]
}
print(travel_log["France"]["cities_vistied"][1])