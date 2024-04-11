from math import ceil

price_one_videocard = int(input())
price_one_prehodnik = int(input())
price_electricity_one_card_per_day = float(input())
profit_one_card_per_day = float(input())
total_price_videocards = 13 * price_one_videocard
total_price_prehodnik = 13 * price_one_prehodnik
price_other_materials = 1000
electricity_consumption = price_electricity_one_card_per_day * 13

total_cost = total_price_videocards + total_price_prehodnik + price_other_materials
income_per_day = (profit_one_card_per_day - price_electricity_one_card_per_day) * 13
number_days_for_balance = ceil(total_cost / income_per_day)

print(f"{total_cost}")
print(f"{number_days_for_balance}")
