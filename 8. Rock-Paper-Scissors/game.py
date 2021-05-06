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

game_choice = input()

if game_choice == '':
    dic_words = ['scissors', 'paper', 'rock']
    print("Okay, let's start")
else:
    dic_words = game_choice.split(',')
    print("Okay, let's start")

while True:
    pc_choice = random.choice(dic_words)

    my_choice = input()

    if my_choice == '!exit':
        print('Bye!')
        break
    elif my_choice == '!rating':
        print(f'Your rating: {rating}')
    elif my_choice == pc_choice:
        print(f'There is a draw ({pc_choice})')
        rating += 50

    elif my_choice == 'rock':  # 'rock'
        if pc_choice in ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'fire':  # 'fire'
        if pc_choice in ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'scissors':  # 'scissors'
        if pc_choice in ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'snake':  # 'snake'
        if pc_choice in ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'human':  # 'human'
        if pc_choice in ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'tree':  # 'tree'
        if pc_choice in ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'wolf':  # 'wolf'
        if pc_choice in ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'sponge':  # 'sponge'
        if pc_choice in ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'paper':  # 'paper'
        if pc_choice in ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'air':  # 'air'
        if pc_choice in ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'water':  # 'water'
        if pc_choice in ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'scissors']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'dragon':  # 'dragon'
        if pc_choice in ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'devil':  # 'devil'
        if pc_choice in ['rock', 'gun', 'lightning', 'human', 'snake', 'scissors', 'fire']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'lightning':  # 'lightning'
        if pc_choice in ['rock', 'gun', 'tree', 'human', 'snake', 'scissors', 'fire']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')

    elif my_choice == 'gun':  # 'gun'
        if pc_choice in ['rock', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']:
            print(f'Well done. The computer chose {pc_choice} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {pc_choice}')
    else:
        print('Invalid input')
