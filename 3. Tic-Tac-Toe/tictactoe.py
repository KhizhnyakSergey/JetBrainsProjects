M = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

print('---------')
print('|', M[0][0], M[0][1], M[0][2], '|')
print('|', M[1][0], M[1][1], M[1][2], '|')
print('|', M[2][0], M[2][1], M[2][2], '|')
print('---------')
count = 2
while True:

    while True:
        try:
            coordinates_wer, coordinates_gor = input("Enter the coordinates: ").split()
            wer = int(coordinates_wer)
            gor = int(coordinates_gor)
            if wer > 3 or wer < 0 or gor > 3 or gor < 0:
                print("Coordinates should be from 1 to 3!")
                continue
            elif M[wer-1][gor-1] == " ":
                if count % 2 == 0:
                    M[wer-1][gor-1] = "X"
                else:
                    M[wer-1][gor-1] = "O"
                count += 1
            elif M[wer-1][gor-1] == "X" or "O":
                print("This cell is occupied! Choose another one!")
                continue
            break
        except ValueError:
            print("You should enter numbers!")

    list_in = [M[0][0], M[0][1], M[0][2], M[1][0], M[1][1], M[1][2], M[2][0], M[2][1], M[2][2]]
    #print(list_in)

    print('---------')
    print('|', M[0][0], M[0][1], M[0][2], '|')
    print('|', M[1][0], M[1][1], M[1][2], '|')
    print('|', M[2][0], M[2][1], M[2][2], '|')
    print('---------')

    # Проверки напобеду
    list_gor_1 = M[0][0], M[0][1], M[0][2]
    list_gor_2 = M[1][0], M[1][1], M[1][2]
    list_gor_3 = M[2][0], M[2][1], M[2][2]

    list_wer_1 = M[0][0], M[1][0], M[2][0]
    list_wer_2 = M[0][1], M[1][1], M[1][2]
    list_wer_3 = M[0][2], M[1][2], M[2][2]

    list_dia_1 = M[0][0], M[1][1], M[2][2]
    list_dia_2 = M[0][2], M[1][1], M[2][0]

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
        elif x == " ":
            num_prop += 1

    for position in list_wins:
        if position[0] == "X" and position[1] == "X" and position[2] == "X":
            winner = position[0]
            wins += 1
            if wins > 1:
                print("Impossible 'if wins > 1:' ")
                break
        elif position[0] == "O" and position[1] == "O" and position[2] == "O":
            winner = position[0]
            wins += 1
            if wins > 1:
                print("Impossible 'if wins > 1:' ")
                break

    if num_x - num_o >= 2 or num_o - num_x >= 2:
        print("Impossible")
    elif wins == 0 and num_prop == 0:
        print("Draw")
        break
    elif num_prop > 0 and wins == 1:
        print(winner, "wins")
        break
    elif wins == 1:
        print(winner, "wins")
        break







