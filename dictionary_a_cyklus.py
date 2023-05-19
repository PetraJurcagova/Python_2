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
    "Draco": 66,
}

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

for jedno_ovoce in ovoce:
    print(jedno_ovoce) # A)vypsani key = nazvy ovoce 


