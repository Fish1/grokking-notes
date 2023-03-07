states_needed = set([
    "mt", "wa", "or", "id", "nv", "ut", "ca", "az"
])

stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}

def get_station_that_covers_most_states(states_needed, stations):
    best_station = None
    best_count = 0
    for station in stations:
        count = 0
        for state in stations[station]:
            if state in states_needed:
                count += 1
        if count > best_count:
            best_station = station
            best_count = count
    if best_station != None:
        for state in stations[best_station]:
            states_needed.discard(state)
    return best_station


min_station = []

station = get_station_that_covers_most_states(states_needed, stations)
while station != None:
    print(station)
    min_station.append(station)
    station = get_station_that_covers_most_states(states_needed, stations)

print(min_station)