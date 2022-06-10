number_pack_of_pen = int(input())
number_pack_of_marker = int(input())
litter_of_board_cleaner = int(input())
percent_of_discount = int(input()) / 100

pens_price = number_pack_of_pen * 5.80
markers_price = number_pack_of_marker * 7.20
board_cleaner = litter_of_board_cleaner * 1.20
total_price = pens_price + markers_price + board_cleaner
total_price -= (percent_of_discount * total_price)


print(total_price)


