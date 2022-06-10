nylon = int(input())
paint = int(input())
thinner = int(input())
worker_hours= int(input())
nylon_price = (nylon + 2) * 1.50
paint_price = (paint * 1.1) * 14.50
thinner_price = thinner * 5
total_price_materials = nylon_price + paint_price + thinner_price + 0.40
total_price_workers = total_price_materials * 0.3 * worker_hours

print(total_price_materials + total_price_workers)