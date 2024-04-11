number_locations = int(input())
expected_daily_production = 0
production_days = 0
daily_production = 0
real_daily_production = 0
total_production = 0
production_counter = 0

for each_location in range(number_locations):
    expected_daily_production = float(input())
    production_days = int(input())
    production_counter = 0                      # NB !!!!!
    for each_day in range(production_days):
        daily_production = float(input())
        production_counter += daily_production
    real_daily_production = production_counter / production_days
    difference = abs(real_daily_production - expected_daily_production)
    if real_daily_production >= expected_daily_production:
        print(f"Good job! Average gold per day: {real_daily_production:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")
