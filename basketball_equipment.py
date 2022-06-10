annual_fee_for_basketball_training = int(input())
price_for_shoes = annual_fee_for_basketball_training * 0.6
price_for_clothes = price_for_shoes * 0.8
price_for_ball = price_for_clothes / 4
price_for_accessories = price_for_ball / 5
total_price = annual_fee_for_basketball_training + price_for_shoes + price_for_clothes + price_for_ball + \
              price_for_accessories
print(total_price)
