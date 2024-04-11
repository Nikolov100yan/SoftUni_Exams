month = input()             # "march", "april", "may", "june", "july", "august"
number_hours = int(input())
number_people = int(input())
daytime = input()           # "day" or "night"
prince_per_person_per_hour = 0

if month in ["march", "april", "may"]:
    if daytime == "day":
        prince_per_person_per_hour = 10.50
    else:
        prince_per_person_per_hour = 8.40
else:
    if daytime == "day":
        prince_per_person_per_hour = 12.60
    else:
        prince_per_person_per_hour = 10.20

if number_people >= 4:
    prince_per_person_per_hour *= 0.9
if number_hours >= 5:
    prince_per_person_per_hour *= 0.5

total_price = number_people * prince_per_person_per_hour * number_hours

print(f"Price per person for one hour: {prince_per_person_per_hour:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
