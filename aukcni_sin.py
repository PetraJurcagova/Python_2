import os
print("Vitejte v programu na tichou drazbu!")


#zajemce = input("Zadejte vase jmeno:\n")
#offer = int(input("Jaka je vase nabidka v KC:\n"))

##pocet_zajemcu = input("Jsou dalsi zajemci? Napiste A nebo N:\n")

#vytvoreni funkce pro jednoho nabizejiciho
#def nabidka (name, cost):
    #kupujici = {}
    #kupujici [name] = cost
    #kupujici ["castka"] = cost
    #print(kupujici)

#nabidka(zajemce,offer)

# naplneni dictionary kupujicimi
lets_continue = "ano"
kupujici = {}

while lets_continue == "ano":
    
    name = input("Jak se jmenujete:\n")
    cost = int(input("Jaka je vase nabidka:\n"))
    kupujici[name] = cost
    lets_continue = input("Jsou dalsi zajemci? Odpovezte 'ano' nebo 'ne'\n")
    if lets_continue == "ne":
        # vycisti obrazovku
        os.system("cls") # os.system("clear") z nejakeho duvodu nefunguje!!!

#print(kupujici)

# zjisteni nejvyssi nabidky
highest_offer = 0

winner = ""

#for key in kupujici:
    #print(kupujici[key])
    #if kupujici[key] > highest_offer:
        #highest_offer = kupujici[key]
        #winner = key
#print(highest_offer)
#print(f"Vitezem tiche aukce se stava {winner} s nabidkou {highest_offer} Kc.")

#hledani viteze
#predchozi cyklus for predelany na funkci
def highest_bid (name): # name zde predstavuje obecny predpis!
    highest_offer = 0
    winner = ""
    for key in name:
         if name[key] > highest_offer:
            highest_offer = name[key]
            winner = key
    print(f"Vitezem tiche aukce se stava {winner} s nabidkou {highest_offer} Kc.")

highest_bid(kupujici)