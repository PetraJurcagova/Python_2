cities = {
    "Spain":"Madrid",
    "France":"Paris",
}

#print(cities)
#print(cities["Spain"])

#dictionary a list
travel_diary = {
    "Spain":["Madrid", "Leon","Valencia"],
    "France":["Paris, Nice","Cannes"],
}

#print(travel_diary["Spain"][1])
#print(travel_diary["Spain"][0])

#dictionary
travel = {
    "Spain":{"visited cities": ["Madrid","Leon","Valencia"],"visits": 5},
    "France":{"visited cities":["Paris, Nice","Cannes"], "visits": 7},
}

#print(travel["Spain"]["visited cities"][1])
#print(travel["France"]["visits"])

#dictionary v listu
traveller = [
    {
        "country":"Spain",
        "visited cities":["Madrid","Leon","Valencia"],
        "visits": 5
    },
    {
        "country":"France",
        "visited cities": ["Paris", "Nice","Cannes"],
        "visits": 3
    },
]
#print(traveller[0]["visited cities"][2])

def zeme(country_n, cities_list, visits_n):
    new_dictionary = {} # zacneme prazdnym dictionary, do ktereho budeme pridavat

    new_dictionary["country"] = country_n
    new_dictionary["visited cities"] = cities_list
    new_dictionary["visits"] = visits_n
    #print(new_dictionary)
    traveller.append (new_dictionary) # napojeni stavajiciho dictionary na novy dictionary
    print(traveller) # nechame vypsat dictionary 


# zavolani funkce, zde zadame parametry do dictionary
zeme ("Italy", ["Roma","Florence", "Neapol"], 7)
zeme ("Czech Republic", ["Prague","Cesky Krumlov", "Cheb"], 5)
zeme ("Austria", ["Wien","Linz", "Graz"], 2)

# zkouska vypsani jednotlivych prvku
print(traveller[2]["visits"]) # 7
print(traveller[1]["visited cities"][1]) # nice