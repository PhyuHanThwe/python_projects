print("Welcome Yumme Curry")
price = {'fired chicken': 2000, 'bubble tea': 1500, 'hot dog': 600, 'juice': 1000}
order = {}

print('        Menu')
print('        ******************')

for menu in price:
    print(menu)

item = input('item: ')
while item != 'OFF':
    quantity = int(input('quantity: '))
    
    if item not in order:
        order[item] = quantity

    else:
        order[item] += quantity    
    item = input('item: ')

print(order)   

bill = 0
for item in order:
    bill += price[item] * order[item]

print("Totl bill", bill)