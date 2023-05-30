# hadaci hra
import random
import os
# Uvodni informace
print("Vitejte ve hre Guess Secret Number")
print("Myslim si cislo od 1 do 100")

# vyreseni obtiznosti


#priprava hry
# potrebujeme secret number

secret_number = random.randint(1, 101)
print(f"Hadane cislo je {secret_number}.")

def obtiznost(): # muzeme a nemusime z toho udelat funkci
    difficulty = input("Vyberte obtiznost: 'easy' nebo 'hard':\n")
    if difficulty == "easy":
        return 7
    elif difficulty == "hard":
        return 4

def guessing_game():
# pocet pokusu
    
    pokusy = obtiznost() # vstupni udaj
   
#print(f"Pocet zbyvajicich pokusu je {pokusy}.") # kontrolni vypis

# rekurze

    another_game = ""
    
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
            another_game = input("Napiste 'yes', pokud chcete pokracovat. Napiste 'no', pokud chcete hru ukoncit.")
            
        # kontrola poctu pokusu   
        if pokusy == 0:
            print("Prohrali jste, pocitac vyhral!")
            another_game = input("Napiste 'yes', pokud chcete pokracovat. Napiste 'no', pokud chcete hru ukoncit.")

        if another_game == "yes":   
            os.system("cls") # vycisteni obrazovky
            guessing_game() # toto je rekurze, funkce je ve funkci, tj. cela se spusti znovu
        elif another_game == "no":
            os.system("cls")
            break # ukonceni cyklu

guessing_game()