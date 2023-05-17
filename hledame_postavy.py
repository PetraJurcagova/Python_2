# hadaci hra, vylepseni o nahodu, vylepseni o pocet pokusu
import random

print("Vitejte v hadaci hre Harry Potter")

characters= ["Harry", "Ron", "Hermionna", "Brumbal"]
character = characters[random.randint(0, len(characters)-1)]
guess = " "

guess_count = 2 # nastaveny pocet pokusu

while character != guess: # dokud je podminka TRUE, tak cyklus jede
    if guess_count != 0: # jeste mame moznost hadat
        guess = input("Uhodnete postavu z filmu Harry Potter.\n")
        guess_count -= 1
    else:
        print(f"Neuhadli jste! Hledane jmeno bylo {character}.")
        break # preruseni cyklu, ktery je jinak nekonecny

    if guess == character: # kontrola spravne odpovedi
        print("Uhadli jste, vybordelne!")   










