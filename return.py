
#def soucet(num1, num2):
    #print(num1 + num2)

#soucet(12,2)
#soucet(45,12)

def better_name(first, second):
    first = first.capitalize() # prvni pismeno bude velke
    second = second.capitalize()
    #print(first, second)
    return f"{first} {second}"
   

# zavolani funkce
result = better_name("petra", "jurcagova")
#better_name("argus", "vyskocil")
print(result)


#jiny zpusob zapsani
def pozdrav (first_n,second_n):
    full = first_n + " " + second_n
    return full.title()

result = pozdrav("petra","jurcagova")
print(result)