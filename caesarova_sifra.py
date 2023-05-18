alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#zakodovani zpravy
def encode(text, shift_number): # shift_number = posun
    for one_letter in text:
        index = alphabet.index(one_letter) # funkce index
        new_index = index + shift_number














