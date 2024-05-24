# import random
#
# # Načítanie slovíčok zo súboru
# with open("obesenec.txt", "r") as file:
#     words = [line.strip() for line in file]
#
# # Náhodný výber slova
# chosen_word = random.choice(words)
#
# # Zobrazenie hádaného slova
# display_word = ["." for _ in chosen_word]
# print(display_word)
#
# # Hádanie písmen
# attempts = 0
# max_attempts = 10
#
# while attempts < max_attempts:
#     guess = input(f"Hádaj písmeno ({max_attempts - attempts} pokusov zostáva): ").lower()
#     if guess in chosen_word:
#         for i, letter in enumerate(chosen_word):
#             print(i,letter)
#             if letter == guess:
#                 display_word[i] = guess
#         print(" ".join(display_word))
#     else:
#         print("Nesprávne písmeno.")
#         attempts += 1
#
#     if "".join(display_word) == chosen_word:
#         print("Gratulujem, uhádol si slovo!")
#         break
#
# if "".join(display_word) != chosen_word:
#     print(f"Hra skončila. Hádané slovo bolo: {chosen_word}")

import random

fr = open('obesenec.txt','r')

words = [line.strip() for line in fr.readlines()]
print(words)

chosen_one = random.choice(words)
print(chosen_one)

display_word = ['.' for i in range(len(chosen_one))]
print(display_word)


attempts = 0
max_attempts = 10

while attempts < max_attempts:
    d = ' '.join(display_word)
    print(d)
    x = input(f'Hadaj pismeno (ostava pocet pokusov {max_attempts-attempts}:')
    if x in chosen_one:
        for i, letter in enumerate(chosen_one):
            if x == letter:
                display_word[i] = x
                attempts += 1
    else:
        print('nespravne pismeno')
        attempts += 1
    if ''.join(display_word) == chosen_one:
        print('Uhadol si slovo!')
        break

if attempts >= max_attempts:
    print(f'maximalny pocet pokusov {max_attempts}prekroceny')
