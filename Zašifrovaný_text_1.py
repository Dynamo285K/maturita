# def sifrovanie(vstup, kluc, desifrovanie):
#     vystup = ""
#     posuny = [(ord(i) - 96) for i in kluc]
#     posun = ""
#     priloz_kluc = ""
#     index = 0
#     for i in vstup:
#         index += 1
#         pos = posuny[index % len(posuny) - 1]
#         if desifrovanie:
#             pos *= -1
#         if i not in pismenka:
#             vystup += i
#             posun += "-"
#             priloz_kluc += kluc[index % len(posuny) - 1]
#         else:
#             vystup += chr((ord(i) - 97 + pos) % 26 + 97)
#             posun += str(pos)
#             priloz_kluc += kluc[index % len(posuny) - 1]
#     if sifra in "sd":
#         return vystup
#     if not desifrovanie and sifra == "n":
#         print("priložený kľúč: {}\nposun: {}\nvýstup: {}".format(priloz_kluc, posun, vystup))
#
# pismenka = "qwertzuiopasdfghjklyxcvbnm"
# vstup = input("vstup: ")
# kluc = input("kľúč: ")
# desifrovanie = False
# sifra = input("šifrovať - s / dešifrovať - d nepracovať so súborom - n: ")
#
# if sifra in "ds":
#     if sifra == "d":
#         desifrovanie = True
#         fr = open("zasifrovany_text_1.txt", "r", encoding="utf-8")
#     else:
#         fr = open("vstupny_text.txt", "r", encoding="utf-8")
#     fw = open("vystup.txt", "w", encoding="utf-8")
#     for riadok in fr.readlines():
#         fw.write(sifrovanie(riadok, kluc, desifrovanie))
# else:
#     sifrovanie(vstup, kluc, desifrovanie)


import string

x = string.ascii_lowercase
print(x)


fr = open('vstupny_text.txt','r',encoding='utf-')


listik = []
for i in fr.readlines():
    listik.append(i.replace('\n','$'))
print(listik)

key = input('kluc')

def sifruj():
    counter = 0
    temp_str = ''
    for i in listik:
        for j in i:
            if j in x:
                r = x.index(key[counter%len(key)])
                f = (x.index(j)+r+1) % 26
                print(r,f)
                temp_str += x[f]
                counter += 1
            else:
                temp_str += j
    print(temp_str)

sifruj()




fp = open('zasifrovany_text_1.txt','r',encoding='utf-')

listik2 = []
for i in fp.readlines():
    listik2.append(i.replace('\n','$'))
print(listik2)


def desifruj():
    temp_str = ''
    counter = 0
    for i in listik2:
        for j in i:
            if j in x:
                r = x.index(key[counter%len(key)]) + 1
                f = x.index(j)-r
                if f < 0:
                    f = 26 + f
                temp_str += x[f]
                counter += 1
            else:
                temp_str += j
    print(temp_str)



desifruj()



