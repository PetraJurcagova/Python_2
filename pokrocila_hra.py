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


#testovani
print(f"testovaci vypis ucet 1: {account_1['follower_count']}")
print(f"testovaci vypis ucet 2: {account_2['follower_count']}")   

# hra
user_answer = input("Kdo ma vice sledovani moznost 'A' nebo 'B'?\n")

right_a = ""
score = 0

if account_1["follower_count"] > account_2["follower_count"]:
    right_a = "A"
else:
    right_a = "B"

if right_a == user_answer:
    score += 1
    print(f"Uhadli jste, vase skore je {score}.")
else:
    print(f"Spatna odpoved, vase konecne skore je {score} bodu.")




