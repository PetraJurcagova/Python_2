# hadaci hra, vylepseni o nahodu
import random
characters= ["Harry", "Ron", "Hermionna", "Brumbal"]
character = characters[random.randint(0, len(characters)-1)]
guess = " "

while character != guess: # dokud je podminka TRUE, tak cyklus jede
    guess = input("Uhodnete postavu z filmu Harry Potter.\n")

print("Uhadli jste, vybordelne!")   







