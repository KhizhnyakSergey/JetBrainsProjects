# Write your code here
import random
my_choice = input()

pc_choice = random.choice(['scissors', 'paper', 'rock'])

my_count = 0
pc_count = 0

if my_choice == 'paper':
    if pc_choice == 'rock':
        my_count += 1
    elif pc_choice == 'scissors':
        pc_count += 1
elif my_choice == 'rock':
    if pc_choice == 'scissors':
        my_count += 1
    elif pc_choice == 'paper':
        pc_count += 1
elif my_choice == 'scissors':
    if pc_choice == 'paper':
        my_count += 1
    elif pc_choice == 'rock':
        pc_count += 1

if my_choice == pc_choice:
    print(f'There is a draw ({pc_choice})')
elif my_count > 0:
    print(f'Well done. The computer chose {pc_choice} and failed')
elif pc_count > 0:
    print(f'Sorry, but the computer chose {pc_choice}')
