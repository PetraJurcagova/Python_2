it_dictionary = {
    "String":"Text",
    "Integer": "Cele cislo",
    "Float": "Desetinne cislo",
    "Blooleane":"Pravda, Nepravda",

}

#for key in it_dictionary:
    #print(key) # vypise string, integer...
    #print(it_dictionary[key]) # vypise value text, cele cislo ...

students_result = {
    "Harry": 85,
    "Ron": 71,
    "Hermionna": 93,
    "Draco": 55,
}

# 91 = excelentni
# 81 = vynikajici
# 71 = splneno
# 61 = nesplneno

hodnoceni = {} # vytvorime prazdny dictionary

for key in students_result:
    #print(key)
    result = ""
    score = students_result[key]
    #print(score)
    if score >= 91:
        result = "excelentni"
    elif score >= 81:
        result = "vynikajici"
    elif score >= 71:
        result = "splneno"
    elif score < 71:
        result = "nesplneno"
    hodnoceni[key] = result

#print(hodnoceni)





zelenina = {
    "paprika": 100,
    "okurka" : 85,
    "zeli" : 140,

}

#100 = dobry
#85 = nedostatek
#140 = prebytek

mnozstvi_zeleniny = {}

for one in zelenina: # vypisuje key = nazvy zeleniny
    #print(one)
    vysledek = ""
    mnozstvi = zelenina[one]
    #print(mnozstvi)
    if mnozstvi == 100:
        vysledek = "dobry"
    elif mnozstvi == 140:
        vysledek = "prebytek"
    elif mnozstvi == 85:
        vysledek = "nedostatek"
    mnozstvi_zeleniny [one] = vysledek
#print(mnozstvi_zeleniny)


ovoce = {
    "meloun": 1000,
    "broskev": 864,
    "pomelo": 715,
}

#1000 = prebytek
#864 = splneno
#715 = nedostatek

# vytvoreni prazdneho dictionary
stav_zasob = {} #2)

for jedno_ovoce in ovoce:
    #print(jedno_ovoce) # A)vypsani key = nazvy ovoce 
    pocet = "" #3) vytvoreni prazdneho stringu, kam se budou ukladat udaje o mnozstvi
    mnozstvi = ovoce[jedno_ovoce] # 4) vypsani podminek
    if mnozstvi == 1000:
        pocet = "prebytek"
    elif mnozstvi == 715:
        pocet = "nedostatek"
    elif mnozstvi == 864:
        pocet = "splneno"
    stav_zasob[jedno_ovoce] = pocet #5) vypsani nov2 naplneneho dictionary
#print(stav_zasob)

zvirata = {
    "kun": 10,
    "morce":5,
    "holub": 2,
}
# 10 = dlouhovekost
#5 = stredni delka
#2 = kratovekost

hodnoceni_veku = {}

for one_animal in zvirata:
    #print(one_animal)
    hodnoceni = ""
    years = zvirata[one_animal]
    if years == 10:
        hodnoceni = "dlouhovekost"
    elif years == 5:
        hodnoceni = "stredni delka"
    elif years == 2:
        hodnoceni = "kratkovekost"
    hodnoceni_veku[one_animal] = hodnoceni

#print(hodnoceni_veku)

students_result = {
    "Harry": 85,
    "Ron": 71,
    "Hermionna": 93,
    "Draco": 55,
}

# 91 = excelentni
# 81 = vynikajici
# 71 = splneno
# 61 = nesplneno

vysledky = {}

for name in students_result:
    #print(name)
    hodnoceni = ""
    key = students_result[name]
    if key >= 91:
        hodnoceni = "excelentni"
    elif key >= 81:
        hodnoceni = "vynikajici"
    elif key >= 71:
        hodnoceni = "splneno"
    elif key < 70:
        hodnoceni = "nesplneno"
    vysledky[name] = hodnoceni

print(vysledky)







