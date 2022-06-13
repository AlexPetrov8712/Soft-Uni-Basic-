name_agency = input()
ticket_adults = int(input())
ticket_kids = int(input())
profit_adults = float(input())
tax = float(input())

kids = profit_adults * 0.30
ticket = kids + tax
tickets_kids = ticket * ticket_kids
adults = profit_adults + tax
ticket_adult = adults * ticket_adults
total = tickets_kids + ticket_adult
g_total = total * 0.20

print(f'The profit of your agency from {name_agency} tickets is {g_total:.2f} lv.')
