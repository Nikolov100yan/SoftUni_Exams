number_bitcoins = int(input())
number_yuans = float(input())
commission_rate = float(input())
usd_rate_in_bgn = 1.76     # bgn
bitcoin_rate_in_bgn = 1168     # bgn
yuan_rate = 0.15 * usd_rate_in_bgn
eur_rate_in_bgn = 1.95     # bgn
amount_bitcoins_in_bgn = number_bitcoins * bitcoin_rate_in_bgn
amount_yuans_in_bgn = number_yuans * yuan_rate
total_amount_bgn = amount_bitcoins_in_bgn + amount_yuans_in_bgn
commission = total_amount_bgn * (commission_rate / 100)
total_amount_bgn -= commission
total_amount_eur = total_amount_bgn / eur_rate_in_bgn
print(f"{total_amount_eur:.2f}")
