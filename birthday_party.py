rent_party_room = float(input())
price_cake = rent_party_room * 0.2
price_drinks = price_cake - (price_cake * 0.45)
price_animator = rent_party_room / 3
total_budget_needed = rent_party_room + price_cake + price_drinks + price_animator
print(total_budget_needed)
