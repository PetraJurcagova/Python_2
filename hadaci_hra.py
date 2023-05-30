# hadaci hra
import random
import os
# Uvodni informace
print("Vitejte ve hre Guess Secret Number")
print("Myslim si cislo od 1 do 100")

#priprava hry
# potrebujeme secret number

secret_number = random.randint(1, 101)
print(f"Hadane cislo je {secret_number}.")

guess_user = int(input("Typnete si cislo:\n"))

if guess_user < secret_number:
    print("Cislo je prilis nizke.")
elif guess_user > secret_number:
    print("Cislo je prilis vysoke.")
else:
    print("Uhadli jste! Pocitac je porazen.")


