# Write your code here
import random

name = input('Enter your name: ')
print(f'Hello, {name}')
with open('rating.txt', 'r') as f:
    for line in f:
        if name in line:
            rating = line.split()
            rating = int(rating[1])
            break
        else:
            rating = 0

while True:

    my_choice = input()
    pc_choice = random.choice(['scissors', 'paper', 'rock'])
    if my_choice != '!rating' and '!exit':
        rating += 50

    if my_choice == '!exit':
        print('Bye!')
        break
    elif my_choice == '!rating':
        print(f'Your rating: {rating}')
    elif my_choice == pc_choice:
        print(f'There is a draw ({pc_choice})')
    elif my_choice == 'paper':
        if pc_choice == 'rock':
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 50
        elif pc_choice == 'scissors':
            print(f'Sorry, but the computer chose {pc_choice}')
    elif my_choice == 'rock':
        if pc_choice == 'scissors':
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 50
        elif pc_choice == 'paper':
            print(f'Sorry, but the computer chose {pc_choice}')
    elif my_choice == 'scissors':
        if pc_choice == 'paper':
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 50
        elif pc_choice == 'rock':
            print(f'Sorry, but the computer chose {pc_choice}')
    else:
        print('Invalid input')
