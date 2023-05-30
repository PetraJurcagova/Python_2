# hadaci hra
import random
import os
# Uvodni informace
print("Vitejte ve hre Guess Secret Number")
print("Myslim si cislo od 1 do 100")

# vyreseni obtiznosti
difficulty = input("Vyberte obtiznost: 'easy' nebo 'hard':\n")

#priprava hry
# potrebujeme secret number

secret_number = random.randint(1, 101)
print(f"Hadane cislo je {secret_number}.")



# pocet pokusu
pokusy = 0 # vstupni udaj
if difficulty == "easy":
    pokusy = 7
elif difficulty == "hard":
    pokusy = 4
#print(f"Pocet zbyvajicich pokusu je {pokusy}.") # kontrolni vypis



while pokusy > 0:
    print(f"Pocet zbyvajicich pokusu je {pokusy}.")
    guess_user = int(input("Typnete si cislo:\n"))

    if guess_user < secret_number:
        print("Cislo je prilis nizke.")
        pokusy -= 1 # odecitame pokusy
    elif guess_user > secret_number:
        print("Cislo je prilis vysoke.")
        pokusy -= 1
    else:
        print("Uhadli jste! Pocitac je porazen.")
     # kontrola poctu pokusu   
    if pokusy == 0:
        print("Prohrali jste, pocitac vyhral!")
