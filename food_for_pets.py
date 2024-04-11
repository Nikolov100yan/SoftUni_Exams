number_days = int(input())
total_quantity_food = float(input())
consumed_dog_food = 0
consumed_cat_food = 0
total_dog_food = 0
total_cat_food = 0
days_counter = 0
biskits = 0
total_number_biskits = 0

for each_day in range(number_days):
    consumed_dog_food = int(input())
    consumed_cat_food = int(input())
    days_counter += 1
    total_dog_food += consumed_dog_food
    total_cat_food += consumed_cat_food
    if days_counter % 3 == 0:
        biskits = (consumed_dog_food + consumed_cat_food) * 0.1
        total_number_biskits += biskits

total_number_biskits = round(total_number_biskits)
percentage_consumed_food = ((total_dog_food + total_cat_food) / total_quantity_food) * 100
percentage_dog_food = (total_dog_food / (total_dog_food + total_cat_food)) * 100
percentage_cat_food = (total_cat_food / (total_dog_food + total_cat_food)) * 100

print(f"Total eaten biscuits: {total_number_biskits}gr.")
print(f"{percentage_consumed_food:.2f}% of the food has been eaten.")
print(f"{percentage_dog_food:.2f}% eaten from the dog.")
print(f"{percentage_cat_food:.2f}% eaten from the cat.")
