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
Depository = {
    "water": {"value": 400, "text": "of water"},
    "milk": {"value": 540, "text": "of milk"},
    "beans": {"value": 120, "text": "of coffee beans"},
    "cups": {"value": 9, "text": "disposable cups"},
    "money": {"sign": "$", "value": 550, "text": "of money"}}


def remaining():
    global Depository
    print("The coffee machine has:")
    print(Depository["water"]["value"], Depository["water"]["text"])
    print(Depository["milk"]["value"], Depository["milk"]["text"])
    print(Depository["beans"]["value"], Depository["beans"]["text"])
    print(Depository["cups"]["value"], Depository["cups"]["text"])
    print(Depository["money"]["sign"] + str(Depository["money"]["value"]), Depository["money"]["text"])
    return action()


def buy():
    global Depository
    a = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")
    if a == '1':
        if Depository["water"]["value"] >= 250 and Depository["beans"]["value"] >= 16 and Depository["cups"]["value"] >= 1:
            print("I have enough resources, making you a coffee!")
            Depository["water"]["value"] -= 250
            Depository["beans"]["value"] -= 16
            Depository["money"]["value"] += 4
            Depository["cups"]["value"] -= 1
        elif Depository["water"]["value"] < 250:
            print("Sorry, not enough water!")
        elif Depository["beans"]["value"] < 16:
            print("Sorry, not enough coffee beans!")
        elif Depository["cups"]["value"] < 1:
            print("Sorry, not enough disposable cups!")
    elif a == '2':
        if Depository["water"]["value"] >= 350 and Depository["beans"]["value"] >= 20 and Depository["milk"]["value"] >= 75 and Depository["cups"]["value"] >= 1:
            print("I have enough resources, making you a coffee!")
            Depository["water"]["value"] -= 350
            Depository["milk"]["value"] -= 75
            Depository["beans"]["value"] -= 20
            Depository["money"]["value"] += 7
            Depository["cups"]["value"] -= 1
        elif Depository["water"]["value"] < 350:
            print("Sorry, not enough water!")
        elif Depository["milk"]["value"] < 75:
            print("Sorry, not enough milk!")
        elif Depository["beans"]["value"] < 20:
            print("Sorry, not enough coffee beans!")
        elif Depository["cups"]["value"] < 1:
            print("Sorry, not enough disposable cups!")
    elif a == '3':
        if Depository["water"]["value"] >= 200 and Depository["beans"]["value"] >= 12 and Depository["milk"]["value"] >= 100 and Depository["cups"]["value"] >= 1:
            print("I have enough resources, making you a coffee!")
            Depository["water"]["value"] -= 200
            Depository["milk"]["value"] -= 100
            Depository["beans"]["value"] -= 12
            Depository["money"]["value"] += 6
            Depository["cups"]["value"] -= 1
        elif Depository["water"]["value"] < 200:
            print("Sorry, not enough water!")
        elif Depository["milk"]["value"] < 100:
            print("Sorry, not enough milk!")
        elif Depository["beans"]["value"] < 12:
            print("Sorry, not enough coffee beans!")
        elif Depository["cups"]["value"] < 1:
            print("Sorry, not enough disposable cups!")
    return action()


def fill():
    global Depository
    Depository["water"]["value"] += int(input("Write how many ml of water do you want to add:\n> "))
    Depository["milk"]["value"] += int(input("Write how many ml of milk do you want to add:\n> "))
    Depository["beans"]["value"] += int(input("Write how many grams of coffee beans do you want to add:\n> "))
    Depository["cups"]["value"] += int(input("Write how many disposable cups of coffee do you want to add:\n> "))
    return action()


def take():
    print("I gave you", Depository["money"]["sign"] + str(Depository["money"]["value"]))
    Depository["money"]["value"] = 0
    return action()


def action():
    while True:
        a = input("Write action (buy, fill, take, remaining, exit):\n> ").lower()
        if a == "buy":
            return buy()
        elif a == "fill":
            return fill()
        elif a == "take":
            return take()
        elif a == "remaining":
            return remaining()
        elif a == "exit":
            break
        else:
            print("error")


action()
'''
