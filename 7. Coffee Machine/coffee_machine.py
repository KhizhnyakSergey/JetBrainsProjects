# Write your code here

water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550
exit_program = False


def remaining():
    global water, milk, coffee_beans, cups, money
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{coffee_beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'${money} of money' + '\n')


def action():
    global exit_program
    print('Write action (buy, fill, take, remaining, exit):')
    str_in = input()
    print()
    if str_in == 'buy':
        buy()
    elif str_in == 'fill':
        fill()
    elif str_in == 'take':
        take()
    elif str_in == 'remaining':
        remaining()
    elif str_in == 'exit':
        exit_program = True


def function_enough():
    global water, milk, coffee_beans, cups, money



def buy():
    global water, milk, coffee_beans, cups, money
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:' + '\n')
    if choice == '1':
        if water >= 250 and coffee_beans >= 16 and cups >= 1:
            water -= 250
            coffee_beans -= 16
            money += 4
            cups -= 1
            print('I have enough resources, making you a coffee!' + '\n')
        elif water < 250:
            print('Sorry, not enough water!' + '\n')
        elif cups < 1:
            print('Sorry, not enough disposable cups!' + '\n')
        elif coffee_beans < 16:
            print('Sorry, not enough coffee beans!' + '\n')
    elif choice == '2':
        if water >= 350 and coffee_beans >= 20 and milk >= 75:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
            cups -= 1
            print('I have enough resources, making you a coffee!' + '\n')
        elif water < 350:
            print('Sorry, not enough water!' + '\n')
        elif cups < 1:
            print('Sorry, not enough disposable cups!' + '\n')
        elif coffee_beans < 20:
            print('Sorry, not enough coffee beans!' + '\n')
        elif milk < 75:
            print('Sorry, not enough milk!' + '\n')
    elif choice == '3':
        if water >= 200 and coffee_beans >= 12 and milk >= 100:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6
            cups -= 1
            print('I have enough resources, making you a coffee!' + '\n')
        elif water < 200:
            print('Sorry, not enough water!' + '\n')
        elif cups < 1:
            print('Sorry, not enough disposable cups!' + '\n')
        elif coffee_beans < 12:
            print('Sorry, not enough coffee beans!' + '\n')
        elif milk < 100:
            print('Sorry, not enough milk!' + '\n')
    elif choice == 'back':
        action()


def fill():
    global water, milk, coffee_beans, cups
    water += int(input('Write how many ml of water do you want to add:'))
    milk += int(input('Write how many ml of milk do you want to add:'))
    coffee_beans += int(input('Write how many grams of coffee beans do you want to add:'))
    cups += int(input('Write how many disposable cups of coffee do you want to add:'))
    print()


def take():
    global money
    print(f'I gave you ${money}' + '\n')
    money = 0


while exit_program == False:
    action()

# Еще одно решение

'''
# Actions
BUY = 'buy'
FILL = 'fill'
TAKE = 'take'

# Coffee types
ESPRESSO = '1'
LATTE = '2'
CAPPUCCINO = '3'

# Stored ingredients
storage = {'MONEY': 550,
           'WATER': 400,
           'MILK': 540,
           'BEANS': 120,
           'CUPS': 9
           }


def make_espresso():
    # espresso cup = 1, water = 250, beans = 16, price = 4
    global storage
    storage['CUPS'] -= 1
    storage['WATER'] -= 250
    storage['BEANS'] -= 16
    storage['MONEY'] += 4
    report()


def make_latte():
    # latte cup = 1, water = 350, milk = 75, beans = 20, price = 7
    global storage
    storage['CUPS'] -= 1
    storage['WATER'] -= 350
    storage['MILK'] -= 75
    storage['BEANS'] -= 20
    storage['MONEY'] += 7
    report()


def make_cappuccino():
    # cappuccino cup = 1, water = 200, milk = 100, beans = 12, price = 6
    global storage
    storage['CUPS'] -= 1
    storage['WATER'] -= 200
    storage['MILK'] -= 100
    storage['BEANS'] -= 12
    storage['MONEY'] += 6
    report()


def report():
    print(f"""
The coffee machine has:
{storage['WATER']} ml of water
{storage['MILK']} ml of milk
{storage['BEANS']} g of coffee beans
{storage['CUPS']} of disposable cups
{storage['MONEY']} of money
""")


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    option = input()
    if option == ESPRESSO:
        make_espresso()
    elif option == LATTE:
        make_latte()
    elif option == CAPPUCCINO:
        make_cappuccino()
    else:
        print("Wrong option")


def fill():
    global storage
    print("Write how many ml of water do you want to add:")
    storage['WATER'] += int(input())
    print("Write how many ml of milk do you want to add:")
    storage['MILK'] += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    storage['BEANS'] += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    storage['CUPS'] += int(input())
    report()


def take():
    global storage
    print(f"I gave you ${storage['MONEY']}")
    storage['MONEY'] = 0
    report()


def coffee_machine():
    report()
    print("Write action (buy, fill, take):")
    option = input()
    if option == BUY:
        buy()
    elif option == FILL:
        fill()
    elif option == TAKE:
        take()
    else:
        print("Wrong input")

coffee_machine()
'''
