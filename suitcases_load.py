capacity = float(input())
luggage_volume = ""
luggage_counter = 0
free_space = capacity

while True:
    luggage_volume = input()
    if luggage_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    else:
        luggage_volume = float(luggage_volume)
    if free_space < luggage_volume:
        print("No more space!")
        break
    luggage_counter += 1
    if luggage_counter % 3 == 0:
        luggage_volume += luggage_volume * 0.1
    free_space -= luggage_volume

print(f"Statistic: {luggage_counter} suitcases loaded.")
