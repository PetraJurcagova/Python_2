import math
print("Vitejte v kalkulatoru na vypocet spotreby barev!")


height = int(input("Zadejte vysku zdi v m:\n"))
weight = int(input("Zadejte sirku zdi v m:\n"))

plocha = height * weight
rozsah = 5


def pocet_plechovek():
    pocet = plocha/rozsah
    if pocet == 1:
        print(f"Celkova spotreba bude {math.ceil(pocet)} plechovka.")
    elif pocet > 1 and pocet < 5:
        print(f"Celkova spotreba bude {math.ceil(pocet)} plechovky.")
    elif pocet >= 5:
        print(f"Celkova spotreba bude {math.ceil(pocet)} plechovek.")

pocet_plechovek()





