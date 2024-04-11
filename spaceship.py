wight = float(input())
length = float(input())
height = float(input())
mean_height_astronauts = float(input())

height_room = mean_height_astronauts + 0.4
volume_room = 2 * 2 * height_room
spaceship_volume = wight * length * height
number_astronauts = spaceship_volume // volume_room

if 3 <= number_astronauts <= 10:
    print(f"The spacecraft holds {number_astronauts:.0f} astronauts.")
elif number_astronauts < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")
