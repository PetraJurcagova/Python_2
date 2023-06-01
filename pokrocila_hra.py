from data import data
import random


# predelani na funkci
def account_generator(all_accounts):
    data_len = len(all_accounts)

    random_number =  random.randint (0, data_len -1)
    return all_accounts [random_number]

    
account_1 = account_generator(data)
account_2 = account_generator(data)

#predelani na funkci, ktera printuje moznosti k porovnani
def printing_options(acc1, acc2):
    print(f"Porovnejte A: {acc1['name']}, {acc1['description']}, {acc1['country']} ")
    print(f"Porovnejte B: {acc2['name']}, {acc2['description']}, {acc2['country']} ")

printing_options(account_1, account_2)