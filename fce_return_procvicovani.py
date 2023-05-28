#year = int(input("Zadejte letopocet, ktery chcete overit:\n"))

#print(f"Zadany letopocet {year} je prestupny.")
#print(f"Zadany letopocet {year} neni prestupny.")

def leap(user_year):
    if user_year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True

    elif user_year % 4 == 0 and year % 100 != 0 :
        return True
    
    else:
        return False


def datum(year, user_month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_result = leap(year)
    if leap_result == True and user_month == 2:
        return 29
    else:
        return days_in_month[user_month - 1]

year = int(input("Zadejte letopocet, ktery chcete overit:\n"))
month = int(input("Zadejte mesic:\n"))

#result = leap(year) # zavolani funkce a protoze pouzivame return, tak musime nasi fci ulozit do resultu
#print(result)
result = datum(year,month)
#print(result)
print(f"Pocet dnu v mesici je {result}.")








