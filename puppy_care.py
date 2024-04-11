available_food = int(input())   # in kg
available_food *= 1000          # in grams
consumed_food = 0

while True:
    command = input()
    if command != "Adopted":
        command = int(command)
        consumed_food += command
    else:
        break

difference = abs(available_food - consumed_food)

if consumed_food <= available_food:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
