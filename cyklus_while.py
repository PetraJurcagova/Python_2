# cyklus pokracuje dokud je nejaka podminka TRUE
x = 0
while x <= 10:
    print(f"Ja jsem {x} cyklus while.") # ctrl +c pro preruseni
    x += 1
print("Jedeme dal.")

# hadaci hra
character = "Harry"
guess = " "

while character != guess: # dokud je podminka TRUE, tak cyklus jede
    guess = input("Uhodnete postavu z filmu Harry Potter\n")

print("Uhadli jste, vybordelne!")   




