from data import data
import random


# predelani na funkci
def account_generator(all_accounts):
    data_len = len(all_accounts)

    random_number =  random.randint (0, data_len -1)
    return all_accounts [random_number]

    
account_1 = account_generator(data)

account_2 = account_generator(data)



