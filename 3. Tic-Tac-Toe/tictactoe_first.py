str_full = input("Enter cells: ")

print('---------')
print('|', str_full[0], str_full[1], str_full[2], '|')
print('|', str_full[3], str_full[4], str_full[5], '|')
print('|', str_full[6], str_full[7], str_full[8], '|')
print('---------')

list_in = list()
for x in str_full:
    list_in.append(x)

# Проверки напобеду
list_gor_1 = list_in[0], list_in[1], list_in[2]
list_gor_2 = list_in[3], list_in[4], list_in[5]
list_gor_3 = list_in[6], list_in[7], list_in[8]

list_wer_1 = list_in[0], list_in[3], list_in[6]
list_wer_2 = list_in[1], list_in[4], list_in[7]
list_wer_3 = list_in[2], list_in[5], list_in[8]

list_dia_1 = list_in[0], list_in[4], list_in[8]
list_dia_2 = list_in[2], list_in[4], list_in[6]

# Список выиграшных комбинаций
list_wins = list_gor_1, list_gor_2, list_gor_3, list_wer_1, list_wer_2, list_wer_3, list_dia_1, list_dia_2

wins = 0
winner = None
num_x = 0
num_o = 0
num_prop = 0

for x in list_in:
    if x == "O":
        num_o += 1
    elif x == "X":
        num_x += 1
    elif x == "_":
        num_prop += 1

for position in list_wins:
    # print(position)
    if position[0] == position[1] == position[2]:
        winner = position[0]
        wins += 1
        if wins > 1:
            print("Impossible")
            break

if num_x - num_o >= 2 or num_o - num_x >= 2:
    print("Impossible")
elif wins == 0 and num_prop == 0:
    print("Draw")
elif num_prop > 0 and wins == 1:
    print(winner, "wins")
elif num_prop > 0 and wins == 0:
    print("Game not finished")
elif wins == 1:
    print(winner, "wins")
