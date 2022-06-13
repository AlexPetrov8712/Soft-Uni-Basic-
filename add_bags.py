price_bags_up_20 = float(input())
kg_bags = float(input())
days = int(input())
number_bags = int(input())
total = price_bags_up_20
if kg_bags <= 10:
    total *= 0.20
elif 10 < kg_bags <= 20:
    total *= 0.50
elif kg_bags > 20:
    total = price_bags_up_20
if days > 30:
    discount = 0.10 * total
    discount_sum = discount + total
    total_sum = number_bags * discount_sum
    print(f'The total price of bags is: {total_sum:.2f} lv.')
elif 7 <= days <= 30:
    discount_7 = 0.15 * total
    discount_77 = discount_7 + total
    total_7 = number_bags * discount_77
    print(f'The total price of bags is: {total_7:.2f} lv.')
elif days < 7:
    discount_1 = 0.40 * total
    discount_10 = discount_1 + total
    total_10 = number_bags * discount_10
    print(f'The total price of bags is: {total_10:.2f} lv.')
