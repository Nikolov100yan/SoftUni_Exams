minutes_walking_per_day = int(input())
number_walks_per_day = int(input())
calories_income_per_day = int(input())
calories_consumption = number_walks_per_day * minutes_walking_per_day * 5

if calories_consumption >= (calories_income_per_day * 0.5):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_consumption}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_consumption}.")
