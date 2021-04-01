# Write your code her
import random

print("H A N G M A N")
print()

survived = ['python', 'java', 'kotlin', 'javascript']
win_word = random.choice(survived)

line_word = '-' * (len(win_word))
# print(line_word)
# print(win_word)

line_word_list = []
win_word_list = []
for x in win_word:
    win_word_list.append(x)
for x in line_word:
    line_word_list.append(x)

lives = 8

while lives > 0:
    print("".join(line_word_list))
    letter = input("Input a letter: ")
    # print()
    if letter in line_word_list:
        print("No improvements")
        lives -= 1
    elif letter in win_word:
        count_let = win_word.count(letter)
        # print("Колическтво букв в слове: ", count_let)
        # print("Буква:", letter)
        ind = win_word.find(letter)

        # print("Индекс буквы в слове:", ind)
        line_word_list[ind] = letter

        if count_let > 1:
            ind = win_word.rfind(letter)
            # print('index второй буквы:', ind)
            line_word_list[ind] = letter
    else:
        print("That letter doesn't appear in the word")
        print()
        lives -= 1

    if "".join(line_word_list) == win_word:
        break

# print(win_word_list)
# print(line_word_list)
player_word = "".join(line_word_list)
# print("Игрок угадал такие буквы:", player_word)
if player_word == win_word:
    print(player_word)
    print("You guessed the word!")
    print("You survived!")
else:
    print("You lost!")
