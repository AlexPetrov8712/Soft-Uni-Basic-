number_chicken_menu = int(input())
number_fish_menu = int(input())
number_veg_menu = int(input())
price_chicken_menu = number_chicken_menu * 10.35
price_fish_menu = number_fish_menu * 12.40
price_veg_menu = number_veg_menu * 8.15
totat_price_of_menu = price_chicken_menu + price_fish_menu + price_veg_menu
price_of_dessert = 0.20 * totat_price_of_menu
price_of_dilivery = 2.50
totat_price = totat_price_of_menu + price_of_dessert + price_of_dilivery
print(totat_price)
