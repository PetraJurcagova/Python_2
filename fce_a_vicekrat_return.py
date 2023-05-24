def pozdrav (first_n,second_n):
    if first_n == "" or second_n == "":
        return "Nevyplnili jste jmeno nebo prijmeni"# return lze pouzit i samostatne nebo s textem
    full = first_n + " " + second_n
    return full.title()
    print("vypis me!") # cokoliv po return uz se neprovede!


#result = pozdrav(input("Vase jmeno: "), input("vase prijmeni: "))
#print(result)


# zkusebni fce na return
def soucet (num1, num2):
    return (num1 + num2) # vraceni
result = soucet(2,1) # vysledek = zavolame funkci a zadame parametry
print(result) # vypsani vysledku


def recept (maso, priloha):
    return f"Kupte {maso} a jako prilohu uvarte {priloha}."

result = recept("hovezi", "brambory")
print(result)

result = recept("kruti", "ryzi")
print(result)