def prvocislo(number_):
    result = "Je to prvocislo!"
    for one in range (2, number_):##rozsah napr: number_ = 12, rozsah bude 2 az 11#
        if number_ % one == 0: # % predstavuje modulo = vypise zbytek po deleni
            result = ("Nejedna se o prvocislo!")
    print(result)



num = int(input("Zadejte cele cislo:\n"))

prvocislo(num) # zavolani funkce, kdy na misto number dosadime cislo zadane uzivatelem = num












