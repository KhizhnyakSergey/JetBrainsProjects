hod = input("Enter cells: ")
str_full = hod
M = [[str_full[0], str_full[1], str_full[2]], [str_full[3], str_full[4], str_full[5]], [str_full[6], str_full[7], str_full[8]]]

print('---------')
print('|', M[0][0], M[0][1], M[0][2], '|')
print('|', M[1][0], M[1][1], M[1][2], '|')
print('|', M[2][0], M[2][1], M[2][2], '|')
print('---------')

while True:
    try:
        coordinates_wer, coordinates_gor = input("Enter the coordinates: ").split()
        wer = int(coordinates_wer)
        gor = int(coordinates_gor)
        if wer > 3 or wer < 0 or gor > 3 or gor < 0:
            print("Coordinates should be from 1 to 3!")
            continue
        elif M[wer-1][gor-1] == "_":
            M[wer-1][gor-1] = "X"
        elif M[wer-1][gor-1] == "X" or "O":
            print("This cell is occupied! Choose another one!")
            continue
        break
    except ValueError:
        print("You should enter numbers!")
print('---------')
print('|', M[0][0], M[0][1], M[0][2], '|')
print('|', M[1][0], M[1][1], M[1][2], '|')
print('|', M[2][0], M[2][1], M[2][2], '|')
print('---------')
