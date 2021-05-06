# Write your code here
import random

while True:
    my_choice = input()
    pc_choice = random.choice(['scissors', 'paper', 'rock'])
    if my_choice == '!exit':
        print('Bye!')
        break
    elif my_choice == pc_choice:
        print(f'There is a draw ({pc_choice})')
    elif my_choice == 'paper':
        if pc_choice == 'rock':
            print(f'Well done. The computer chose {pc_choice} and failed')
        elif pc_choice == 'scissors':
            print(f'Sorry, but the computer chose {pc_choice}')
    elif my_choice == 'rock':
        if pc_choice == 'scissors':
            print(f'Well done. The computer chose {pc_choice} and failed')
        elif pc_choice == 'paper':
            print(f'Sorry, but the computer chose {pc_choice}')
    elif my_choice == 'scissors':
        if pc_choice == 'paper':
            print(f'Well done. The computer chose {pc_choice} and failed')
        elif pc_choice == 'rock':
            print(f'Sorry, but the computer chose {pc_choice}')
    else:
        print('Invalid input')

