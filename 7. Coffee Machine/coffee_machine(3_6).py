# Write your code here
water = int(input('Write how many ml of water the coffee machine has:'))
milk = int(input('Write how many ml of milk the coffee machine has:'))
coffee = int(input('Write how many grams of coffee beans the coffee machine has:'))
how_cups_needs = int(input('Write how many cups of coffee you will need:'))
count = 0

while True:
    # print(water, milk, coffee)
    # print(how_cups_needs)
    # print(count)
    if water >= 200 and milk >= 50 and coffee >= 15:
        water -= 200
        milk -= 50
        coffee -= 15
        count += 1
    elif water < 200 or milk < 50 or coffee < 15:
        break

if count == how_cups_needs:
    print('Yes, I can make that amount of coffee')
elif count > how_cups_needs:
    differ = count - how_cups_needs
    print(f'Yes, I can make that amount of coffee (and even {differ} more than that)')
elif count < how_cups_needs:
    print(f'No, I can make only {count} cups of coffee')
