fruit = input()         # "Watermelon", "Mango", "Pineapple" or "Raspberry"
pack_size = input()     # "small" or "big"
number_packs = int(input())
flacon_price = 0
number_flacons = 0

if pack_size == "small":
    number_flacons = 2
    if fruit == "Watermelon":
        flacon_price = 56
    elif fruit == "Mango":
        flacon_price = 36.66
    elif fruit == "Pineapple":
        flacon_price = 42.10
    elif fruit == "Raspberry":
        flacon_price = 20
elif pack_size == "big":
    number_flacons = 5
    if fruit == "Watermelon":
        flacon_price = 28.70
    elif fruit == "Mango":
        flacon_price = 19.60
    elif fruit == "Pineapple":
        flacon_price = 24.80
    elif fruit == "Raspberry":
        flacon_price = 15.20

total_price = number_packs * flacon_price * number_flacons

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f"{total_price:.2f} lv.")
