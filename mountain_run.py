record_in_seconds = float(input())
distance_in_meters = float(input())
speed_per_second = float(input())

slope_effect = (distance_in_meters // 50) * 30
real_speed = (speed_per_second * distance_in_meters) + slope_effect
difference = abs(record_in_seconds - real_speed)

if real_speed < record_in_seconds:
    print(f" Yes! The new record is {real_speed:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")
