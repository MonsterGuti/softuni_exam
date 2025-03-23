import re

places_on_the_map = input()

pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"

matches = re.findall(pattern, places_on_the_map)

destinations = [match[1] for match in matches]

total_points = sum(len(destination) for destination in destinations)

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {total_points}")
