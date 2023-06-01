from data import data
import random

data_len = len(data)
#print(data_len)
#random.randint(len(data))
random_number_1 =  random.randint (0, data_len -1)
random_number_2 = random.randint(0, data_len -1)

print(random_number_1) #, kontrolni vypis

# vygenerujeme dva nahodne ucty
account_1 = data [random_number_1]

account_2 = data [random_number_2]

print(account_1)
print(account_2)


