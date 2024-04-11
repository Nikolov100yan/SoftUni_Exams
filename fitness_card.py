available_budget = float(input())
sex = input()                       # 'm' or 'f'
age = int(input())
sport = input()
price_fitness_card = 0

if sex == 'm':
    if sport == "Gym":
        price_fitness_card = 42
    elif sport == "Boxing":
        price_fitness_card = 41
    elif sport == "Yoga":
        price_fitness_card = 45
    elif sport == "Zumba":
        price_fitness_card = 34
    elif sport == "Dances":
        price_fitness_card = 51
    elif sport == "Pilates":
        price_fitness_card = 39
elif sex == 'f':
    if sport == "Gym":
        price_fitness_card = 35
    elif sport == "Boxing":
        price_fitness_card = 37
    elif sport == "Yoga":
        price_fitness_card = 42
    elif sport == "Zumba":
        price_fitness_card = 31
    elif sport == "Dances":
        price_fitness_card = 53
    elif sport == "Pilates":
        price_fitness_card = 37

if age <= 19:
    price_fitness_card *= 0.8

difference = price_fitness_card - available_budget

if available_budget >= price_fitness_card:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${difference:.2f} more.")
