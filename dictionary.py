# datovy typ dictionary
# key = value, slovo = preklad

it_dictionary = {
    "String":"Text",
    "Integer": "Cele cislo",
    "Float": "Desetinne cislo",
    "Blooleane":"Pravda, Nepravda",

}

print(it_dictionary["String"]) # musime napsat key, funguje jako indentifikator
print(it_dictionary["Float"])

it_dictionary_2 = {
    2:"Text",
    10: "Cele cislo",
    17: "Desetinne cislo",
    25:"Pravda, Nepravda",
}

#print(it_dictionary_2[25])
#print(it_dictionary_2[17])

# pridani hodnot
it_dictionary_2[107] = "ulozeni dalsi hodnoty"
print(it_dictionary_2)

#prazdny dictionary
empty = {}

#vyprazdnit d
#it_dictionary_2 = {}

# menime hodnoty
it_dictionary_2[107] = "Textova hodnota"
print(it_dictionary_2)